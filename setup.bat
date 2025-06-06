@echo off
echo Setting up the environment...

:: Define the virtual environment directory name
set VENV_DIR=venv

:: Check if Python is available
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: Python not found. Please install Python 3.7+ and make sure it's added to your system's PATH.
    echo You can download Python from https://www.python.org/downloads/windows/
    goto end
)
echo Found Python.

:: Create a virtual environment if it doesn't exist
if not exist %VENV_DIR% (
    echo Creating virtual environment "%VENV_DIR%"...
    python -m venv %VENV_DIR%
    if %errorlevel% neq 0 (
        echo Error: Failed to create virtual environment. Check Python installation.
        goto end
    )
    echo Virtual environment created.
) else (
    echo Virtual environment "%VENV_DIR%" already exists. Skipping creation.
)

:: Activate the virtual environment
echo Activating virtual environment...
call %VENV_DIR%\Scripts\activate.bat
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

:: --- Install PyTorch (CPU version by default) ---
:: Installing CPU version as it works on all systems.
:: Users with compatible NVIDIA GPUs will need to UPGRADE manually later.
echo Installing PyTorch CPU version (works on all systems)...
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
if %errorlevel% neq 0 (
    echo Error: Failed to install PyTorch CPU version. See error above.
    goto deactivate_and_end
) else (
    echo PyTorch CPU version installed successfully.
)

echo.
echo --- SETUP COMPLETE ---
echo Environment "%VENV_DIR%" created/activated and dependencies installed.
echo.
echo The CPU version of PyTorch has been installed.
echo Image generation will be much slower on CPU compared to a compatible NVIDIA GPU.
echo.
echo You can run the application using run.bat.
echo.

goto end

:deactivate_and_end
:: Deactivate the virtual environment before exiting on error
echo Deactivating virtual environment...
deactivate
echo.

:end
echo Press any key to exit...
pause
