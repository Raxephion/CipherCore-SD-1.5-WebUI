# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 2024

@author: raxephion
Basic Stable Diffusion 1.5 Gradio App with local/Hub models and CPU/GPU selection
Added multi-image generation capability.
Modified to download Hub models to local MODELS_DIR (set to "checkpoints").
"""

import gradio as gr
import torch
from diffusers import StableDiffusionPipeline
# Import commonly used schedulers
from diffusers import DDPMScheduler, EulerDiscreteScheduler, DPMSolverMultistepScheduler, LMSDiscreteScheduler
import os
from PIL import Image
import time # Optional: for timing generation
import random # Needed for random seed
import numpy as np # Needed for MAX_SEED, even if not used directly with gr.Number(-1) input


# --- Configuration ---
MODELS_DIR = "checkpoints" # Local directory for storing/caching all models
# Standard SD 1.5 sizes (multiples of 64 are generally safe)
SUPPORTED_SD15_SIZES = ["512x512", "768x512", "512x768", "768x768", "1024x768", "768x1024", "1024x1024", "hire.fix"]

# Mapping of friendly scheduler names to their diffusers classes
SCHEDULER_MAP = {
    "Euler": EulerDiscreteScheduler,
    "DPM++ 2M": DPMSolverMultistepScheduler,
    "DDPM": DDPMScheduler,
    "LMS": LMSDiscreteScheduler,
}
DEFAULT_SCHEDULER = "Euler"

DEFAULT_HUB_MODELS = [
    "Raxephion/Typhoon-SD15-V1",
    "Yntec/RevAnimatedV2Rebirth",
    "stablediffusionapi/realcartoon-anime-v11",
    "Raxephion/Typhoon-SD15-V2",
    "stablediffusionapi/realistic-vision",
    "stablediffusionapi/dreamshaper8"
]

# --- Constants for UI / Generation ---
MAX_SEED = np.iinfo(np.int32).max

# --- Determine available devices and set up options ---
AVAILABLE_DEVICES = ["CPU"]
if torch.cuda.is_available():
    AVAILABLE_DEVICES.append("GPU")
    print(f"CUDA available. Found {torch.cuda.device_count()} GPU(s).")
    if torch.cuda.device_count() > 0:
        print(f"Using GPU 0: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA not available. Running on CPU.")

DEFAULT_DEVICE = "GPU" if "GPU" in AVAILABLE_DEVICES else "CPU"

# --- Global state for the loaded pipeline ---
current_pipeline = None
current_model_id = None
current_device_loaded = None

# --- Helper function to list available local models ---
def list_local_models(models_dir_param): # Renamed param to avoid conflict if MODELS_DIR was global and function arg
    if not os.path.exists(models_dir_param):
        os.makedirs(models_dir_param)
        print(f"Created directory: {models_dir_param}")
        return []
    local_models = [os.path.join(models_dir_param, d) for d in os.listdir(models_dir_param)
                    if os.path.isdir(os.path.join(models_dir_param, d))]
    return local_models

# --- Image Generation Function ---
def generate_image(model_identifier, selected_device_str, prompt, negative_prompt, steps, cfg_scale, scheduler_name, size, seed, num_images):
    global current_pipeline, current_model_id, current_device_loaded, SCHEDULER_MAP, MAX_SEED, MODELS_DIR # MODELS_DIR is used here

    if not model_identifier or model_identifier == "No models found":
        raise gr.Error(f"No model selected or available. Please add models to '{MODELS_DIR}' or ensure Hub IDs are correct in the script.")
    if not prompt:
        raise gr.Error("Please enter a prompt.")

    num_images_int = int(num_images)
    if num_images_int <= 0:
         raise gr.Error("Number of images must be at least 1.")

    device_to_use = "cuda" if selected_device_str == "GPU" and "GPU" in AVAILABLE_DEVICES else "cpu"
    if selected_device_str == "GPU" and device_to_use == "cpu":
         raise gr.Error("GPU selected but CUDA is not available to PyTorch. Ensure you have a compatible NVIDIA GPU, the correct drivers, and have installed the CUDA version of PyTorch in your environment.")

    dtype_to_use = torch.float32
    if device_to_use == "cuda":
        if torch.cuda.is_available() and torch.cuda.get_device_capability(0)[0] >= 7:
             dtype_to_use = torch.float16
             print("GPU supports FP16, using torch.float16 for potential performance/memory savings.")
        else:
             dtype_to_use = torch.float32
             print("GPU might not fully support FP16 or capability check failed, using torch.float32.")
    else:
         dtype_to_use = torch.float32

    print(f"Attempting generation on device: {device_to_use}, using dtype: {dtype_to_use}")

    if current_pipeline is None or current_model_id != model_identifier or (current_device_loaded is not None and str(current_device_loaded) != device_to_use):
        print(f"Loading model: {model_identifier} onto {device_to_use}...")
        if current_pipeline is not None:
             print(f"Unloading previous model '{current_model_id}' from {current_device_loaded}...")
             if str(current_device_loaded) == "cuda":
                  try:
                      current_pipeline.to("cpu")
                      print("Moved previous pipeline to CPU.")
                  except Exception as move_e:
                      print(f"Warning: Failed to move previous pipeline to CPU: {move_e}")
             del current_pipeline
             current_pipeline = None
             if str(current_device_loaded) == "cuda":
                 try:
                     torch.cuda.empty_cache()
                     print("Cleared CUDA cache.")
                 except Exception as cache_e:
                     print(f"Warning: Error clearing CUDA cache: {cache_e}")

        if device_to_use == "cuda":
             if not torch.cuda.is_available():
                  raise gr.Error("CUDA selected but not available. Please install PyTorch with CUDA support or select CPU.")

        try:
            is_local_path = os.path.isdir(model_identifier)

            if is_local_path:
                 print(f"Attempting to load local model from: {model_identifier}")
                 pipeline = StableDiffusionPipeline.from_pretrained(
                     model_identifier,
                     torch_dtype=dtype_to_use,
                     safety_checker=None,
                 )
            else: # This is the block for Hub models
                 # MODELS_DIR (which is "checkpoints") is used here
                 print(f"Attempting to load Hub model: {model_identifier} into local cache: {MODELS_DIR}")
                 pipeline = StableDiffusionPipeline.from_pretrained(
                     model_identifier,
                     torch_dtype=dtype_to_use,
                     safety_checker=None,
                     cache_dir=MODELS_DIR
                 )

            pipeline = pipeline.to(device_to_use)
            current_pipeline = pipeline
            current_model_id = model_identifier
            current_device_loaded = torch.device(device_to_use)

            unet_config = getattr(pipeline, 'unet', None)
            if unet_config and hasattr(unet_config, 'config') and hasattr(unet_config.config, 'cross_attention_dim'):
                 cross_attn_dim = unet_config.config.cross_attention_dim
                 if cross_attn_dim != 768:
                     warning_msg = (f"Warning: Loaded model '{model_identifier}' might not be a standard SD 1.x model "
                                    f"(expected UNet cross_attention_dim 768, found {cross_attn_dim}). "
                                    "Results may be unexpected or generation might fail.")
                     print(warning_msg)
                     gr.Warning(warning_msg)
                 else:
                     print("UNet cross_attention_dim is 768, consistent with SD 1.x.")
            else:
                 print("Could not check UNet cross_attention_dim.")

            print(f"Model '{model_identifier}' loaded successfully on {current_device_loaded} with dtype {dtype_to_use}.")

        except Exception as e:
            current_pipeline = None
            current_model_id = None
            current_device_loaded = None
            print(f"Error loading model '{model_identifier}': {e}")
            error_message_lower = str(e).lower()
            if "cannot find requested files" in error_message_lower or "404 client error" in error_message_lower or "no such file or directory" in error_message_lower:
                 raise gr.Error(f"Model '{model_identifier}' not found. Check name/path or internet connection. Error: {e}")
            elif "checkpointsnotfounderror" in error_message_lower or "valueerror: could not find a valid model structure" in error_message_lower:
                 raise gr.Error(f"No valid diffusers model at '{model_identifier}'. Ensure it's a diffusers format directory or a valid Hub ID. Error: {e}")
            elif "out of memory" in error_message_lower:
                 raise gr.Error(f"Out of Memory (OOM) loading model. Try a lighter model or select CPU. Error: {e}")
            elif "cusolver64" in error_message_lower or "cuda driver version" in error_message_lower or "cuda error" in error_message_lower:
                 raise gr.Error(f"CUDA/GPU Driver Error: {e}. Check drivers, PyTorch with CUDA installation, or select CPU.")
            elif "safetensors_rust.safetensorserror" in error_message_lower or "oserror: cannot load" in error_message_lower or "filenotfounderror" in error_message_lower:
                 raise gr.Error(f"Model file error for '{model_identifier}': {e}. Files might be corrupt, incomplete, or the path is wrong.")
            elif "could not import" in error_message_lower or "module not found" in error_message_lower:
                 raise gr.Error(f"Dependency error: {e}. Ensure all dependencies are installed and PyTorch is installed correctly for your device.")
            else:
                raise gr.Error(f"Failed to load model '{model_identifier}': {e}")

    if current_pipeline is None:
         raise gr.Error("Model failed to load. Cannot generate image.")

    selected_scheduler_class = SCHEDULER_MAP.get(scheduler_name)
    if selected_scheduler_class is None:
         print(f"Warning: Unknown scheduler '{scheduler_name}'. Using default: {DEFAULT_SCHEDULER}.")
         selected_scheduler_class = SCHEDULER_MAP[DEFAULT_SCHEDULER]
         gr.Warning(f"Unknown scheduler '{scheduler_name}'. Using default: {DEFAULT_SCHEDULER}.")

    try:
        scheduler_config = current_pipeline.scheduler.config
        current_pipeline.scheduler = selected_scheduler_class.from_config(scheduler_config)
        print(f"Scheduler set to: {scheduler_name}")
    except Exception as e:
        print(f"Error setting scheduler '{scheduler_name}': {e}")
        try:
             print(f"Attempting to fallback to default scheduler: {DEFAULT_SCHEDULER}")
             current_pipeline.scheduler = SCHEDULER_MAP[DEFAULT_SCHEDULER].from_config(scheduler_config)
             gr.Warning(f"Failed to set scheduler to '{scheduler_name}', fell back to {DEFAULT_SCHEDULER}. Error: {e}")
        except Exception as fallback_e:
             print(f"Fallback scheduler failed too: {fallback_e}")
             raise gr.Error(f"Failed to configure scheduler '{scheduler_name}' and fallback failed. Error: {e}")

    width, height = 512, 768
    if size.lower() == "hire.fix":
        width, height = 1024, 1024
        print(f"Interpreting 'hire.fix' size as {width}x{height}")
    else:
        try:
            w_str, h_str = size.split('x')
            width = int(w_str)
            height = int(h_str)
        except ValueError:
            raise gr.Error(f"Invalid size format: '{size}'. Use 'WidthxHeight' (e.g., 512x512) or 'hire.fix'.")
        except Exception as e:
             raise gr.Error(f"Error parsing size '{size}': {e}")

    multiple_check = 64
    if width % multiple_check != 0 or height % multiple_check != 0:
         warning_msg_size = (f"Warning: Image size {width}x{height} is not a multiple of {multiple_check}. "
                             f"Stable Diffusion 1.5 models are typically trained on sizes like 512x512 or 768x768. "
                             "Using non-standard sizes may cause tiling, distortions, or other artifacts.")
         print(warning_msg_size)
         gr.Warning(warning_msg_size)

    generator = None
    generator_device = current_pipeline.device if current_pipeline else torch.device(device_to_use)
    seed_int = int(seed)

    if seed_int == -1:
        seed_int = random.randint(0, MAX_SEED)
        print(f"User requested random seed (-1), generated: {seed_int}")
    else:
        print(f"Using provided seed: {seed_int}")

    try:
        generator = torch.Generator(device=generator_device).manual_seed(seed_int)
        print(f"Generator set with seed {seed_int} on device: {generator_device}")
    except Exception as e:
         print(f"Warning: Error setting seed generator on device {generator_device}: {e}. Falling back to default generator or system random.")
         gr.Warning(f"Failed to set seed generator with seed {seed_int}. Using random seed. Error: {e}")
         generator = None
         pass

    print(f"Generating {num_images_int} image(s): Prompt='{prompt[:80]}{'...' if len(prompt) > 80 else ''}', NegPrompt='{negative_prompt[:80]}{'...' if len(negative_prompt) > 80 else ''}', Steps={int(steps)}, CFG={float(cfg_scale)}, Size={width}x{height}, Scheduler={scheduler_name}, Seed={seed_int if generator else 'System Random'}, Images={num_images_int}")
    start_time = time.time()

    try:
        num_inference_steps_int = int(steps)
        guidance_scale_float = float(cfg_scale)

        if num_inference_steps_int <= 0 or guidance_scale_float <= 0:
             raise ValueError("Steps and CFG Scale must be positive values.")
        if width <= 0 or height <= 0:
             raise ValueError("Image width and height must be positive.")

        output = current_pipeline(
            prompt=prompt,
            negative_prompt=negative_prompt if negative_prompt else None,
            num_inference_steps=num_inference_steps_int,
            guidance_scale=guidance_scale_float,
            width=width,
            height=height,
            generator=generator,
            num_images_per_prompt=num_images_int,
        )
        end_time = time.time()
        print(f"Generation finished in {end_time - start_time:.2f} seconds.")
        generated_images_list = output.images
        actual_seed_used = seed_int if generator else -1
        return generated_images_list, actual_seed_used

    except gr.Error as e:
         raise e
    except ValueError as ve:
         print(f"Parameter Error: {ve}")
         raise gr.Error(f"Invalid Parameter: {ve}")
    except Exception as e:
        print(f"An error occurred during image generation: {e}")
        error_message_lower = str(e).lower()
        if "size must be a multiple of" in error_message_lower or "invalid dimensions" in error_message_lower or "shape mismatch" in error_message_lower:
             raise gr.Error(f"Image generation failed - Invalid size '{width}x{height}' for model: {e}. Try a multiple of 64 or 8.")
        elif "out of memory" in error_message_lower or "cuda out of memory" in error_message_lower:
             print("Hint: Try smaller image size, fewer steps, fewer images, or a model that uses less VRAM.")
             raise gr.Error(f"Out of Memory (OOM) during generation. Try smaller size/steps, fewer images, or select CPU. Error: {e}")
        elif "runtimeerror" in error_message_lower:
             raise gr.Error(f"Runtime Error during generation: {e}. This could be a model/scheduler incompatibility or other issue.")
        elif "device-side assert" in error_message_lower or "cuda error" in error_message_lower:
             raise gr.Error(f"CUDA/GPU Error during generation: {e}. Ensure PyTorch with CUDA is correctly installed and compatible.")
        elif "expected all tensors to be on the same device" in error_message_lower:
             raise gr.Error(f"Device mismatch error during generation: {e}. This is an internal error, please report it.")
        else:
             raise gr.Error(f"Image generation failed: An unexpected error occurred. {e}")

# --- Gradio Interface ---
# list_local_models is called with MODELS_DIR (which is "checkpoints")
local_models_list = list_local_models(MODELS_DIR)
model_choices = local_models_list + DEFAULT_HUB_MODELS

if not model_choices:
    initial_model_choices = ["No models found"]
    initial_default_model = "No models found"
    model_dropdown_interactive = False
    print(f"\n--- IMPORTANT ---")
    print(f"No local models in '{MODELS_DIR}' and no default Hub models listed.") # Uses MODELS_DIR
    print(f"Place diffusers SD 1.5 models in '{os.path.abspath(MODELS_DIR)}' or add Hub IDs to DEFAULT_HUB_MODELS in script.") # Uses MODELS_DIR
    print(f"-----------------\n")
else:
    initial_model_choices = model_choices
    if "Raxephion/Typhoon-SD15-V1" in model_choices:
         initial_default_model = "Raxephion/Typhoon-SD15-V1"
    elif local_models_list: # Changed from local_models to local_models_list
         initial_default_model = local_models_list[0]
    else:
         initial_default_model = model_choices[0]
    model_dropdown_interactive = True

scheduler_choices = list(SCHEDULER_MAP.keys())

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        f"""
        # CipherCore Stable Diffusion 1.5 Generator
        Create images with Stable Diffusion 1.5. Supports local models from `./{MODELS_DIR}`
        and/or select models from the drop-down menu. Selected models will auto-download if not already cached.
        _Note: 'hire.fix' size option currently generates at 1024x1024._
        """ # Uses MODELS_DIR
    )

    with gr.Row():
        with gr.Column(scale=2):
            model_dropdown = gr.Dropdown(
                choices=initial_model_choices,
                value=initial_default_model,
                label=f"Select Model (Local from ./{MODELS_DIR} or Hugging Face Hub)", # Uses MODELS_DIR
                interactive=model_dropdown_interactive,
            )
            device_dropdown = gr.Dropdown(
                choices=AVAILABLE_DEVICES,
                value=DEFAULT_DEVICE,
                label="Processing Device",
                interactive=len(AVAILABLE_DEVICES) > 1,
            )
            prompt_input = gr.Textbox(label="Positive Prompt", placeholder="e.g., a majestic lion in a vibrant jungle, photorealistic", lines=3, autofocus=True)
            negative_prompt_input = gr.Textbox(label="Negative Prompt (Optional)", placeholder="e.g., blurry, low quality, deformed, watermark", lines=2)

            with gr.Accordion("Advanced Settings", open=False):
                with gr.Row():
                    steps_slider = gr.Slider(minimum=5, maximum=150, value=20, label="Inference Steps", step=1)
                    cfg_slider = gr.Slider(minimum=1.0, maximum=30.0, value=7.5, label="CFG Scale", step=0.1)
                with gr.Row():
                     scheduler_dropdown = gr.Dropdown(
                        choices=scheduler_choices,
                        value=DEFAULT_SCHEDULER,
                        label="Scheduler"
                    )
                     size_dropdown = gr.Dropdown(
                        choices=SUPPORTED_SD15_SIZES,
                        value="512x512",
                        label="Image Size"
                    )
                with gr.Row():
                     seed_input = gr.Number(label="Seed (-1 for random)", value=-1, precision=0)
                     num_images_slider = gr.Slider(
                         minimum=1,
                         maximum=4,
                         value=1,
                         step=1,
                         label="Number of Images",
                         interactive=True
                     )

            generate_button = gr.Button("✨ Generate Image ✨", variant="primary", scale=1)

        with gr.Column(scale=3):
            output_gallery = gr.Gallery(
                label="Generated Images",
                show_label=True,
                show_share_button=True,
                show_download_button=True,
                interactive=False
            )
            actual_seed_output = gr.Number(label="Actual Seed Used", precision=0, interactive=False)

    generate_button.click(
        fn=generate_image,
        inputs=[
            model_dropdown,
            device_dropdown,
            prompt_input,
            negative_prompt_input,
            steps_slider,
            cfg_slider,
            scheduler_dropdown,
            size_dropdown,
            seed_input,
            num_images_slider
        ],
        outputs=[output_gallery, actual_seed_output],
        api_name="generate"
    )

    gr.Markdown(
        f"""
        ---
        **Usage Notes:**
        1. Place local Diffusers-compatible SD 1.5 models into the `{MODELS_DIR}` folder or update model list in main.py.
        2. Select a model from the dropdown (local or Hub). Hub models will be downloaded to `{MODELS_DIR}`.
        3. Choose your processing device (GPU recommended if available).
        4. Enter your positive and optional negative prompts.
        5. Adjust advanced settings (Steps, CFG Scale, Scheduler, Size, Seed, Number of Images) if needed.
        6. Click "Generate Image".
        The first generation with a new model/device might take some time to load.
        Generating multiple images increases VRAM and time requirements. Start with 1-2 images if you have limited VRAM.
        If you have a compatible NVIDIA GPU and want faster generation, you'll need to upgrade PyTorch to the CUDA version *after* running setup.bat. See the instructions printed in the setup console.
        """ # Uses MODELS_DIR
    )

if __name__ == "__main__":
    print("\n--- Starting CipherCore Stable Diffusion 1.5 Generator ---")
    cuda_status = "CUDA available" if torch.cuda.is_available() else "CUDA not available"
    gpu_count_str = f"Found {torch.cuda.device_count()} GPU(s)." if torch.cuda.is_available() else ""

    print(f"{cuda_status} {gpu_count_str}")
    print(f"Available devices detected by PyTorch: {', '.join(AVAILABLE_DEVICES)}")
    print(f"Default device selected by app: {DEFAULT_DEVICE}")
    # MODELS_DIR (which is "checkpoints") is used here
    print(f"Models will be loaded from/cached to: {os.path.abspath(MODELS_DIR)}")

    if not model_choices:
         print(f"\n!!! WARNING: No models available. The Gradio app will launch but cannot generate images. Please add models to '{MODELS_DIR}' or list Hub IDs in main.py. !!!") # Uses MODELS_DIR
    else:
         # Changed local_models to local_models_list here
         print(f"Found {len(local_models_list)} local model(s) in '{os.path.abspath(MODELS_DIR)}'.") # Uses MODELS_DIR

    print("Launching Gradio interface...")
    demo.launch(show_error=True, inbrowser=True)
    print("Gradio interface closed.")
