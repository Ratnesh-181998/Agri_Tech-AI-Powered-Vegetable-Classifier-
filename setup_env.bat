@echo off
echo ===================================================
echo Ninjacart CV Classification - Environment Setup
echo ===================================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b
)

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Upgrading pip...
python -m pip install --upgrade pip

echo Installing dependencies from requirements.txt...
if exist requirements.txt (
    pip install -r requirements.txt
    echo Dependencies installed successfully.
) else (
    echo Warning: requirements.txt not found!
)

echo.
echo ===================================================
echo Setup Complete!
echo To start working, run: venv\Scripts\activate
echo Then launch Jupyter: jupyter notebook
echo ===================================================
pause
