@echo off
echo Setting up the environment for Perchance Revival (GPU)...

:: Define the virtual environment directory name
set VENV_DIR=venv

:: Change directory to the script's location
cd /d "%~dp0"

:: Check if Python is available
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: Python not found. Please install Python 3.8+ and make sure it's added to your system's PATH.
    echo You can download Python from https://www.python.org/downloads/windows/
    goto end
)
echo Found Python.

:: Create virtual environment if it doesn't exist
if not exist %VENV_DIR% (
    echo Creating virtual environment "%VENV_DIR%"...
    python -m venv %VENV_DIR%
    if %errorlevel% neq 0 (
        echo Error: Failed to create virtual environment. Check Python installation or permissions.
        goto end
    )
    echo Virtual environment created.
) else (
    echo Virtual environment "%VENV_DIR%" already exists. Skipping creation.
)

:: Activate the virtual environment
echo Activating virtual environment...
call "%VENV_DIR%\Scripts\activate.bat"
if %errorlevel% neq 0 (
    echo Error: Failed to activate virtual environment. Check virtual environment setup.
    goto end
)
echo Virtual environment activated.

:: Install core dependencies from requirements.txt
echo Installing core dependencies from requirements.txt...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install core dependencies from requirements.txt.
    echo Ensure requirements.txt exists and is correct. See error above.
    goto deactivate_and_end
)
echo Core dependencies installed successfully.

:: Install PyTorch with CUDA 12.8
echo.
echo Attempting to install PyTorch with CUDA 12.8...
echo This assumes you have a compatible NVIDIA GPU and the correct drivers.

set CUDA_VERSION=cu128
echo Using CUDA version: %CUDA_VERSION%
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/%CUDA_VERSION%

if %errorlevel% neq 0 (
    echo.
    echo !!! ERROR: Failed to install PyTorch with CUDA support !!!
    echo.
    echo This installation step failed. Possible reasons:
    echo - Incompatible or missing NVIDIA GPU drivers
    echo - Incorrect CUDA version (%CUDA_VERSION%)
    echo - Internet or pip issues
    echo.
    echo To troubleshoot:
    echo - Run 'nvidia-smi' in Command Prompt to check your driver's CUDA version
    echo - Visit https://pytorch.org/get-started/locally/ for exact install commands
    echo - Try this CPU-only fallback (slower, but works):
    echo   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
    echo.
    goto deactivate_and_end
) else (
    echo.
    echo PyTorch installed successfully with CUDA 12.8.
)

echo.
echo --- SETUP COMPLETE ---
echo Environment "%VENV_DIR%" created/activated and dependencies installed.
echo You can now run the application using run.bat.
echo.

goto end

:deactivate_and_end
:: Deactivate the virtual environment before exiting on error
echo Deactivating virtual environment...
call "%VENV_DIR%\Scripts\deactivate.bat"
echo.

:end
echo Press any key to exit...
pause >nul
