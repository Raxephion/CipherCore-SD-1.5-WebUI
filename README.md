# CipherCore - Stable Diffusion 1.5 Image Generator Web UI (CPU & GPU)

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome to the CipherCore Stable Diffusion 1.5 Generator! This user-friendly Gradio web application allows you to effortlessly generate images using various Stable Diffusion 1.5 models. Whether you have local models or prefer popular ones from the Hugging Face Hub, this tool provides a simple interface to unleash your creativity on your CPU or GPU.

This repository includes simple batch files (`setup.bat`, `run.bat`) to streamline the setup and running process specifically for **Windows** users, aiming to make it easier for those less familiar with command-line interfaces.

## ✨ Features

*   **Flexible Model Selection:**
    *   Load your own Stable Diffusion 1.5 models (in `diffusers` format) from a local `./checkpoints` directory.
    *   Access a curated list of popular SD1.5 models directly from the Hugging Face Hub (models are downloaded and cached locally on first use).
*   **Device Agnostic:**
    *   Run inference on your **CPU**.
    *   Leverage your **NVIDIA GPU** for significantly faster generation (requires installing the CUDA-enabled PyTorch version). **The default setup installs the CPU version; instructions are provided to upgrade for GPU users.**
*   **Comprehensive Control:**
    *   **Positive & Negative Prompts:** Guide the AI with detailed descriptions of what you want (and don't want).
    *   **Inference Steps:** Control the number of denoising steps.
    *   **CFG Scale:** Adjust how strongly the image should conform to your prompt.
    *   **Schedulers:** Experiment with different sampling algorithms (Euler, DPM++ 2M, DDPM, LMS).
    *   **Image Sizes:** Choose from standard SD1.5 resolutions, plus a "hire.fix" option (interpreted as 1024x1024).
    *   **Seed Control:** Set a specific seed for reproducible results or use -1 for random generation.
*   **User-Friendly Interface:**
    *   Clean and intuitive Gradio UI.
    *   Organized controls with advanced settings in an accordion for a cleaner look.
    *   Direct image display with download and share options.
*   **Safety First (Note):** The built-in safety checker is **disabled** in this version to allow for maximum creative freedom. Please be mindful of the content you generate.

## 🚀 Prerequisites

*   **Windows Operating System:** The provided batch files (`.bat`) are for Windows. For other operating systems, follow the manual setup steps below.
*   **Python:** 3.8 or higher. Ensure Python is installed and added to your system's PATH (usually an option during installation). You can download Python from [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/).
*   **Git:** For cloning the repository.
*   **Hardware:**
    *   A modern CPU is required.
    *   For GPU acceleration (optional but highly recommended for speed), a compatible NVIDIA GPU with up-to-date CUDA drivers. At least 6-8GB VRAM is recommended for 512x512 generation, more for larger sizes.
*   **Internet Connection:** Required for downloading models from Hugging Face Hub on first use.

## ⚙️ Setup & Installation (Windows via Batch Files)

1.  **Clone the Repository:** Open Command Prompt or PowerShell, navigate to where you want to download the project, and run:
    ```bash
    git clone https://github.com/Raxephion/CipherCore-SD1.5-Image-Generator-.git
    cd CipherCore-SD1.5-Image-Generator-
    ```
    *(Note: If you cloned to a different directory name, replace `CipherCore-SD1.5-Image-Generator-` above with your chosen directory name.)*

2.  **Run the Setup Script:**
    Double-click the `setup.bat` file in the project's root directory OR run it from your command prompt:
    ```bash
    setup.bat
    ```
    *   This script will create a Python virtual environment (`venv`), install the necessary core dependencies (like Gradio, Diffusers, Transformers, Hugging Face Hub, Pillow) from `requirements.txt`, and install the **CPU version** of PyTorch by default.
    *   **Important:** Read the output in the command prompt carefully during and after the script finishes. It will provide specific commands if you wish to upgrade PyTorch to the GPU-accelerated CUDA version, which is necessary for fast generation on an NVIDIA GPU. You must run this upgrade command manually if you have a GPU and want to use it.

3.  **Prepare Local Models (Optional):**
    *   Create a directory named `checkpoints` in the root of the project (if `setup.bat` didn't create it).
    *   Place your Stable Diffusion 1.5 models (in `diffusers` format – meaning each model is a folder containing files like `model_index.json`, `unet/`, `vae/`, etc.) inside the `checkpoints` directory.
        Example structure:
        ```
        CipherCore-SD1.5-Image-Generator-/
        ├── checkpoints/
        │   ├── my-custom-model-1/
        │   │   ├── model_index.json
        │   │   ├── unet/
        │   │   └── ...
        │   └── another-local-model/
        │       └── ...
        ├── main.py
        ├── requirements.txt
        ├── setup.bat
        ├── run.bat
        └── ...
        ```

## ▶️ Running the Application (Windows via Batch File)

Once the setup is complete, launch the Gradio web UI:

Double-click the `run.bat` file in the project's root directory OR run it from your command prompt:

```bash
run.bat
