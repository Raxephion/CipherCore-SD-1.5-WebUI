# CipherCore - Stable Diffusion 1.5 Image Generator Web UI (CPU & GPU)

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome to the CipherCore Stable Diffusion 1.5 Generator! This user-friendly Gradio web application allows you to effortlessly generate images using various Stable Diffusion 1.5 models. Whether you have local models or prefer popular ones from the Hugging Face Hub, this tool provides a simple interface to unleash your creativity on your CPU or GPU.

This project is designed for **Windows** users seeking a simple experience through easy-to-use batch files, as well as providing manual setup options for other platforms or advanced users.

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
*   **Git:** (Required for manual setup and updating) For cloning the repository.
*   **Hardware:**
    *   A modern CPU is required.
    *   For GPU acceleration (optional but highly recommended for speed), a compatible NVIDIA GPU with up-to-date CUDA drivers. At least 6-8GB VRAM is recommended for 512x512 generation, more for larger sizes.
*   **Internet Connection:** Required for downloading models from Hugging Face Hub and for updates.

## 📦 Easy Setup (Windows - Download & Run)

This is the recommended method for most Windows users.

1.  **Download the project:**
    *   Go to the GitHub repository page: `(https://github.com/Raxephion/CipherCore-WebUI)`
    *   Click the green "Code" button.
    *   Click "Download ZIP".
2.  **Extract the ZIP:** Extract the downloaded ZIP file to a location on your computer (e.g., your Documents folder or Desktop). This will create a folder like `CipherCore-SD1.5-Image-Generator-main` (or similar). Rename it if you prefer.
3.  **Run the Setup Script:**
    *   Navigate into the extracted folder.
    *   Find the file named `setup.bat`.
    *   **Double-click `setup.bat`** to run it.
    *   A command prompt window will open. Follow the instructions in the window. This script will create a Python virtual environment (`venv`), install all necessary core dependencies, and install the **CPU version** of PyTorch by default.
    *   **Important:** Read the output in the command prompt carefully during and after the script finishes. It will provide specific commands if you wish to upgrade PyTorch to the GPU-accelerated CUDA version, which is necessary for fast generation on an NVIDIA GPU. You must run this upgrade command manually if you have a GPU and want to use it.
4.  **Prepare Local Models (Optional):**
    *   Inside the extracted project folder, create a directory named `checkpoints` (if `setup.bat` didn't create it).
    *   Place your Stable Diffusion 1.5 models (in `diffusers` format – meaning each model is a folder containing files like `model_index.json`, `unet/`, `vae/`, etc.) inside the `checkpoints` directory.
        Example structure:
        ```
        YourProjectFolder/
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
        ├── update.bat
        └── ...
        ```

## ▶️ Running the Application (Windows - Easy Method)

Once the setup is complete, launch the Gradio web UI by double-clicking the `run.bat` file in the project folder.

*   A command prompt window will open, activate the environment, and start the application.
*   A browser window should automatically open to the application (or a local URL will be provided in the console, usually `http://127.0.0.1:7860`).

## 🔄 Updating the Application (Windows - Easy Method)

To get the latest code and dependency updates from this repository after using the easy setup:

*   Navigate to the project folder.
*   Find the file named `update.bat`.
*   **Double-click `update.bat`** to run it.
*   A command prompt window will open and pull the latest changes from the GitHub repository and upgrade the Python packages in your virtual environment.
*   **Important:** This assumes you have not made local changes that conflict with the repository updates. If `git pull` fails, you may need to handle merge conflicts manually or discard local changes.

---

## ⚙️ Manual Setup (Windows - Git Clone)

This method is for Windows users who are comfortable with Git.

1.  **Clone the Repository:** Open Command Prompt or PowerShell, navigate to where you want to download the project, and run:
    ```bash
    git clone https://github.com/Raxephion/CipherCore-SD1.5-Image-Generator-.git
    cd CipherCore-SD1.5-Image-Generator-
    ```
    *(Note: If you cloned to a different directory name, replace `CipherCore-SD1.5-Image-Generator-` above with your chosen directory name.)*
2.  **Proceed with Batch Files:** Continue by following **Step 2 (Run the Setup Script)**, **Step 3 (Prepare Local Models)**, **Running**, and **Updating** instructions from the **📦 Easy Setup (Windows - Download & Run)** section above.

## 🛠️ Manual Setup, Running & Updating (For Linux/macOS or Advanced Users)

If you are not on Windows or prefer a manual command-line approach:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Raxephion/CipherCore-SD1.5-Image-Generator-.git
    cd CipherCore-SD1.5-Image-Generator-
    ```
2.  **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3.  **Install Dependencies (including PyTorch):**
    *   Install core dependencies (this includes `gradio`, `diffusers`, `transformers`, `huggingface_hub`, `Pillow`):
        ```bash
        pip install -r requirements.txt
        ```
    *   Install PyTorch: **This step is crucial and depends on your hardware.**
        *   **For CPU ONLY:**
            ```bash
            pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
            ```
        *   **For NVIDIA GPU with CUDA (Recommended for speed):** Find the appropriate command for your CUDA version (check PyTorch's website: [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)). Example for CUDA 11.8:
            ```bash
            pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
            ```
4.  **Prepare Local Models (Optional):** Follow Step 3 from the **📦 Easy Setup (Windows - Download & Run)** section above.
5.  **Run the Application:**
    ```bash
    python main.py
    ```
    Ensure your virtual environment is activated (`source venv/bin/activate`) before running this command.
6.  **Updating Manually:**
    *   Navigate to the project directory in your terminal.
    *   Ensure your virtual environment is activated (`source venv/bin/activate`).
    *   Pull the latest code: `git pull`
    *   Update dependencies: `pip install -r requirements.txt --upgrade`
    *   Deactivate the environment: `deactivate`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) file for details.
