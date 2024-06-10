# Azayd_IT_Consultancy

## Django Project Initialization Guide

## Prerequisites

- Python 3.x installed on your system
- `pip` (Python package installer)

#### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/your-repo.git
```

### Step 2: Create Virtual Environment
```bash
python -m venv env
```
#### Activate the virtual environment:

* On Windowos:
```bash
.\env\Scripts\activate
```
* On macOS and Linux:
```bash
  source env/bin/activate
```
### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
#### If requirements.txt does not exist, create it and add Django:
```bash
pip install django
pip freeze > requirements.txt
```

### Step 4: Create and Configure Django Project
#### If you haven't created a Django project yet, you can do so with the following command:
```bash
django-admin startproject project-name
```
#### Navigate into your project directory:
```bash
cd project-name
```

## Install SQL Database

### Step 5: Install Database Driver
#### For this example, we will use PostgreSQL. You need to install the psycopg2 package, which is the PostgreSQL adapter for Python:
```bash
pip install psycopg2-binary
```
### Step 6: Configure Database in `settings.py`
#### Open the settings.py file in your project directory and configure the database settings. Replace the default SQLite settings with PostgreSQL settings:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your-db-name',
        'USER': 'your-db-user',
        'PASSWORD': 'your-db-password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Step 7: Apply Migrations
#### Apply initial migrations to set up your database:
```bash
python manage.py makemigrations
python manage.py migrate
```
### Step 8: Create a Superuser
#### Create a superuser to access the Django admin interface:
```bash
python manage.py createsuperuser
```

### Step 9: Run the Development Server
```bash
python manage.py runserver
```



