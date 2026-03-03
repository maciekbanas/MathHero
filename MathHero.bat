@echo off
setlocal

REM Launcher for MathHero (Windows)
cd /d "%~dp0"

if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" "src\main.py"
    goto :end
)

py -3 "src\main.py"
if %errorlevel% neq 0 (
    echo.
    echo Nie udalo sie uruchomic gry przez 'py -3'. Probuje przez 'python'...
    python "src\main.py"
)

:end
endlocal
pause
