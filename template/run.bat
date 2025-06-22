@echo off
echo Setting up and starting Pitfall Adventure...

REM Navigate to root directory
cd ..

REM Check if venv_win exists, if not create it
if not exist "venv_win" (
    echo Creating virtual environment venv_win...
    python -m venv venv_win
)

REM Activate virtual environment
echo Activating virtual environment...
call venv_win\Scripts\activate.bat

REM Install/update requirements
echo Installing requirements...
pip install -r requirements.txt

REM Navigate back to pitfallgame directory
cd pitfallgame

REM Start web server and open browser
echo Starting Pitfall Adventure Web Server...
echo Opening browser at http://localhost:8000
echo.
start "" http://localhost:8000
python -m http.server 8000

pause