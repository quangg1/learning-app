#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running collectstatic..."
python manage.py collectstatic --no-input

echo "Removing old migrations..."
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

echo "Making migrations for web_app..."
python manage.py makemigrations web_app --noinput

echo "Running migrations..."
python manage.py migrate --noinput

echo "Running migrations for specific apps..."
python manage.py migrate auth --noinput
python manage.py migrate admin --noinput
python manage.py migrate sessions --noinput
python manage.py migrate web_app --noinput

echo "Creating default roles if they don't exist..."
python manage.py shell << END
from web_app.models import Role
roles = ['Student', 'Instructor', 'Admin']
for role_name in roles:
    Role.objects.get_or_create(role_name=role_name)
END

echo "Verifying database tables..."
python manage.py shell << END
from django.db import connection
tables = connection.introspection.table_names()
print("Available tables:", tables)
if 'user' not in tables:
    print("WARNING: 'user' table is missing!")
if 'role' not in tables:
    print("WARNING: 'role' table is missing!")
END

echo "Build completed successfully!" 