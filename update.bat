@echo off
echo Updating the CipherCore Stable Diffusion 1.5 Generator...

:: Define the virtual environment directory name (must match setup.bat and run.bat)
set VENV_DIR=venv
set REPO_URL=https://github.com/Raxephion/CipherCore-SD-1.5-WebUI
set TEMP_DIR=temp_extraction

:: Change directory to the script's location
cd /d "%~dp0"

:: Check if Git is available
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo Git not found. Attempting to initialize a Git repository...
    echo (This will download the latest code but won't track future changes without Git installed.)

    :: Create a temporary directory for extraction
    mkdir %TEMP_DIR%
    if %errorlevel% neq 0 (
        echo Error: Failed to create temporary directory.
        goto end
    )

    :: Download the repository as a ZIP file if Git is not installed
    powershell -Command "(New-Object System.Net.WebClient).DownloadFile('%REPO_URL%/archive/refs/heads/main.zip', 'repo.zip')"
    if %errorlevel% neq 0 (
        echo Error: Failed to download repository as ZIP. Check internet connection.
        rmdir /s /q %TEMP_DIR% 2>nul
        goto end
    )

    echo Extracting ZIP file to temporary directory...
    powershell -Command "Expand-Archive -Path 'repo.zip' -DestinationPath '%TEMP_DIR%'"
    if %errorlevel% neq 0 (
        echo Error: Failed to extract ZIP file.
        del repo.zip
        rmdir /s /q %TEMP_DIR% 2>nul
        goto end
    )

    echo Moving files from temporary directory to current directory...
    for /d %%d in (%TEMP_DIR%\*) do (
        for %%f in ("%%d\*") do (
            move /y "%%f" "." >nul
        )
    )

    echo Removing ZIP file...
    del repo.zip
    if %errorlevel% neq 0 (
        echo Warning: Failed to delete ZIP file.
    )

    echo Removing temporary directory...
    rmdir /s /q %TEMP_DIR%
    if %errorlevel% neq 0 (
        echo Warning: Failed to delete temporary directory.
    )

    echo Successfully downloaded and extracted latest code from GitHub.
    echo Please install git for proper version control - https://git-scm.com/

    goto update_dependencies
)

echo Found Git.

:: Check if the virtual environment exists
if not exist %VENV_DIR%\Scripts\activate.bat (
    echo Error: Virtual environment "%VENV_DIR%" not found.
    echo Please run setup.bat first to create the environment.
    goto end
)

:: Activate the virtual environment
echo Activating virtual environment...
call %VENV_DIR%\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo Error: Failed to activate virtual environment. Check virtual environment setup.
    goto end
)
echo Virtual environment activated.

:: Pull latest code from the repository
echo Pulling latest code from GitHub...
git pull
if %errorlevel% neq 0 (
    echo Error: Failed to pull latest code. This could be due to local changes, network issues, or Git configuration.
    echo Please resolve the Git issue manually or discard local changes if necessary.
    goto deactivate_and_end
)
echo Code updated successfully.

:update_dependencies
:: Install/Upgrade dependencies from requirements.txt
echo Installing/Upgrading dependencies from requirements.txt...
pip install -r requirements.txt --upgrade
if %errorlevel% neq 0 (
    echo Error: Failed to install/upgrade dependencies. See the output above for details.
    echo This could be due to network issues or conflicts between packages.
    goto deactivate_and_end
)
echo Dependencies updated successfully.

echo.
echo --- UPDATE COMPLETE ---
echo The application code and dependencies are now up-to-date.
echo.
echo If you have a compatible NVIDIA GPU and manually installed the CUDA version of PyTorch,
echo this update should not affect that. If you encounter GPU issues, re-run the specific
echo PyTorch CUDA installation command from the setup instructions while the environment is active.
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
