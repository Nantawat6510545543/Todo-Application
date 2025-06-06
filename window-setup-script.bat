@echo off

:: Check if py is available, if not, check if python3 is available, if not, fall back to python
where py > nul 2>&1
if %errorlevel%==0 (
    set PYTHON_CMD=py
) else (
    where python3 > nul 2>&1
    if %errorlevel%==0 (
        set PYTHON_CMD=python3
    ) else (
        set PYTHON_CMD=python
    )
)

echo Setting up the project environment...
%PYTHON_CMD% -m venv venv
call .\venv\Scripts\activate

echo Install requirements..
pip install -r requirements.txt

echo Create .env file...
copy sample.env .env

echo Run migrations...
%PYTHON_CMD% manage.py migrate

echo Run Server...
$PYTHON_CMD manage.py runserver