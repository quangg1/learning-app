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

echo "Making migrations..."
python manage.py makemigrations --noinput

echo "Running migrations in order..."
# First migrate contenttypes (required for auth)
python manage.py migrate contenttypes --noinput
# Then migrate auth
python manage.py migrate auth --noinput
# Then migrate admin (depends on auth)
python manage.py migrate admin --noinput
# Then migrate sessions
python manage.py migrate sessions --noinput
# Then migrate your app
python manage.py migrate web_app --noinput
# Finally run a general migrate to catch any dependencies
python manage.py migrate --noinput

echo "Verifying database setup..."
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
    required_tables = ['auth_user', 'role', 'userrole']
    missing_tables = [table for table in required_tables if table not in tables]
    if missing_tables:
        raise Exception(f"Missing required tables: {missing_tables}")
    print("All required tables exist!")
END

echo "Creating default roles..."
python manage.py shell << END
from web_app.models import Role
roles = ['Student', 'Instructor', 'Admin']
for role_name in roles:
    role, created = Role.objects.get_or_create(role_name=role_name)
    print(f"Role '{role_name}' {'created' if created else 'already exists'}")
END

echo "Creating superuser..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print("Superuser created!")
else:
    print("Superuser already exists!")
END

echo "Build completed successfully!" 