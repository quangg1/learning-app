#!/usr/bin/env bash
# exit on error
set -o errexit
cd back_end_learning_app
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running collectstatic..."
python manage.py collectstatic --no-input --clear

echo "Setting up database schema..."
python manage.py shell << END
from django.db import connection
with connection.cursor() as cursor:
    # Create schema if not exists
    cursor.execute("CREATE SCHEMA IF NOT EXISTS public;")
    # Grant permissions
    cursor.execute("GRANT ALL ON SCHEMA public TO learning_app_db_user;")
    cursor.execute("GRANT ALL ON SCHEMA public TO public;")
END

echo "Making fresh migrations..."
python manage.py makemigrations
python manage.py makemigrations web_app

echo "Running migrations..."
# Run migrations in sequence
python manage.py migrate auth --fake-initial
python manage.py migrate --fake-initial
python manage.py migrate web_app --fake-initial

# Run migrations again without fake
python manage.py migrate auth
python manage.py migrate
python manage.py migrate web_app

echo "Creating initial data..."
python manage.py shell << END
from web_app.models import Role
from django.contrib.auth import get_user_model
User = get_user_model()

# Create roles
roles = ['Student', 'Instructor', 'Admin']
for role_name in roles:
    Role.objects.get_or_create(role_name=role_name)

# Create superuser if not exists
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
END

echo "Verifying database setup..."
python manage.py shell << END
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("SELECT tablename FROM pg_tables WHERE schemaname = 'public';")
    tables = cursor.fetchall()
    if not tables:
        raise Exception("No tables found in public schema!")
    print("Found tables:", [table[0] for table in tables])
END

echo "Build completed!" 