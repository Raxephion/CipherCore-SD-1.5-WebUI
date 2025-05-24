@echo off
echo Activating virtual environment and running app...

:: Define the virtual environment directory name (must match setup.bat)
set VENV_DIR=venv

:: Check if the virtual environment exists
if not exist %VENV_DIR%\Scripts\activate.bat (
    echo Error: Virtual environment "%VENV_DIR%" not found. Please run setup.bat first.
    goto end
)

:: Activate the virtual environment
call %VENV_DIR%\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo Error: Failed to activate virtual environment.
    goto end
)
echo Virtual environment activated.

:: Run the main Python script
echo Starting the Gradio app...
python main.py
if %errorlevel% neq 0 (
     echo Error: The application encountered an error. See the output above for details.
) else (
     echo Application finished.
)


:: Deactivate the virtual environment
echo Deactivating virtual environment...
deactivate

:end
echo Press any key to exit...
pause
