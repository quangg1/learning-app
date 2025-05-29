#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running collectstatic..."
python manage.py collectstatic --no-input

echo "Checking database connection..."
python manage.py shell << END
import os
import dj_database_url
from django.db import connections
from django.db.utils import OperationalError

db_url = os.getenv('DATABASE_URL') or os.getenv('DB_URL')
if not db_url:
    raise Exception("DATABASE_URL is not set!")

config = dj_database_url.parse(db_url)
try:
    conn = connections['default']
    conn.cursor()
    print("Database connection successful!")
except OperationalError:
    raise Exception("Could not connect to database!")
END

echo "Making migrations for web_app..."
python manage.py makemigrations web_app --noinput

echo "Showing migrations plan..."
python manage.py showmigrations

echo "Running migrations..."
python manage.py migrate auth --noinput
python manage.py migrate contenttypes --noinput
python manage.py migrate admin --noinput
python manage.py migrate sessions --noinput
python manage.py migrate web_app --noinput

echo "Verifying database tables..."
python manage.py shell << END
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
    """)
    tables = [row[0] for row in cursor.fetchall()]
    print("Available tables:", tables)
    required_tables = ['user', 'role', 'userrole']
    for table in required_tables:
        if table not in tables:
            print(f"WARNING: '{table}' table is missing!")
END

echo "Creating default roles if they don't exist..."
python manage.py shell << END
from web_app.models import Role
roles = ['Student', 'Instructor', 'Admin']
for role_name in roles:
    role, created = Role.objects.get_or_create(role_name=role_name)
    print(f"Role '{role_name}' {'created' if created else 'already exists'}")
END

echo "Build completed successfully!" 