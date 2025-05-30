@echo off
echo Starting Learning App locally...

:: Remove old virtual environments if they exist
if exist "back-end-learning-app\venv" rmdir /s /q "back-end-learning-app\venv"
if exist "front-end-learning-app\venv" rmdir /s /q "front-end-learning-app\venv"

:: Create and activate virtual environment for backend
echo Setting up backend...
cd back-end-learning-app
python -m venv venv
if not exist "venv\Scripts\activate.bat" (
    echo Failed to create backend virtual environment
    exit /b 1
)
call venv\Scripts\activate.bat

:: Install backend dependencies
pip install -r requirements.txt

:: Setup database
python manage.py makemigrations web_app
python manage.py migrate

:: Create superuser if not exists
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin') if not User.objects.filter(username='admin').exists() else None"

:: Start backend server in a new window
start cmd /k "cd back-end-learning-app && call venv\Scripts\activate.bat && python manage.py runserver 0.0.0.0:8000"

:: Setup frontend
cd ../front-end-learning-app

:: Create and activate virtual environment for frontend
python -m venv venv
if not exist "venv\Scripts\activate.bat" (
    echo Failed to create frontend virtual environment
    exit /b 1
)
call venv\Scripts\activate.bat

:: Install frontend dependencies
pip install -r requirements.txt
pip install python-dotenv

:: Create .env file for frontend
echo API_BE=learning-app> .env
echo DOMAIN_BE=http://localhost:8000>> .env
echo TURN_ON_SCREEN=false>> .env
echo PORT=8550>> .env
echo DEBUG=true>> .env

:: Set environment variables
set PORT=8550
set PYTHONPATH=%cd%

:: Start frontend server
start cmd /k "cd front-end-learning-app && call venv\Scripts\activate.bat && set PORT=8550 && set PYTHONPATH=%cd% && python main.py"

echo Learning App is running!
echo Backend: http://localhost:8000
echo Frontend: http://localhost:8550
echo Admin interface: http://localhost:8000/admin
echo Username: admin
echo Password: admin

:: Keep the window open
pause 