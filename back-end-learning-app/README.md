### Setup environment

Pre-requisites:
- PostgreSQL
- Python version: 3.9+

```bash
# Create a virtual environment before running the next command
# Ctrl + Shift + P -> Python: Create Virtual Environment
.venv/Scripts/activate
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

#### Create .env file

Create a file named `.env` in the root directory of the project and add the following content:

```
SECRET_KEY=secret
DEBUG=True    # Set to True for local development
API_ROUTE=db-name     # Default: "learning-app"
HOST_BE_LOCAL=localhost:8000
DB_URL=postgresql://postgres:<password>@<localhost>:<port>/<db-name>    # Change password, host, port, db-name
FRONT_END_URL=http://localhost:3000 
ADMIN_TEMPLATES=True
```

#### Create database

!THIS STEP IS MANDATORY OR THE NEXT STEP WILL FAIL!
Use the pgAdmin tool to create a new database. (pgAdmin should be installed along with PostgreSQL)
The name should be the same as the value of the `API_ROUTE` variable in the `.env` file.

```bash
python manage.py makemigrations
python manage.py migrate
```

#### Import test data

```bash
python manage.py loaddata backup/test_data.json
```

### Run the project

```bash
python manage.py runserver
```
