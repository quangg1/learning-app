#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running collectstatic..."
python manage.py collectstatic --no-input

echo "Making migrations..."
python manage.py makemigrations --noinput

echo "Running migrations..."
python manage.py migrate --noinput

echo "Creating default roles if they don't exist..."
python manage.py shell << END
from web_app.models import Role
roles = ['Student', 'Instructor', 'Admin']
for role_name in roles:
    Role.objects.get_or_create(role_name=role_name)
END

echo "Build completed successfully!" 