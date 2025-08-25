# store-api
`Techforge project for backend`

# Install virtual env
`python3 -m venv store_env`

# Active virtual environment
`source store_env/bin/activate`

# Install Django
`pip install django`

# Verify dependecies in the virtual environment
`pip freeze`

# Create project django
`django-admin startproject store`

# Start up project
`python3 manage.py runserver`

# Save dependecies in requirement file
`pip freeze > requirements.txt`

# Clone repository
`git clone https://github.com/Jojo190503/shop_api.git`
`cd shop_api`

# Install dependecies
`pip install -r requirements.txt`

# Configure PostgreSQL database
`Configure PostgreSQL in shop_api/settings.py`

# Apply migrations
`python manage.py migrate`

# Create superuser
`python manage.py createsuperuser`

# API Endpoints
`GET /api/categories/` : Liste des catégories
`POST /api/register/` : Inscription d'un utilisateur
`GET /api/transactions/` : Liste des transactions

# Features
`Gestion des utilisateurs, boutiques, articles, et transactions`
`Interface d'administration Django pour gérer les données`
`Validation de la force des mots de passe via l'interface client`
