echo # Shop API > README.md
echo. >> README.md
echo Une API RESTful pour gérer un centre commercial, permettant aux utilisateurs de payer des articles dans différentes boutiques enregistrées. >> README.md
echo. >> README.md
echo ## Prérequis >> README.md
echo - Python 3.8+ >> README.md
echo - PostgreSQL >> README.md
echo - Django >> README.md
echo - Django REST Framework >> README.md
echo. >> README.md
echo ## Installation >> README.md
echo 1. Cloner le dépôt : >> README.md
echo    ```bash >> README.md
echo    git clone https://github.com/Jojo190503/shop_api.git >> README.md
echo    cd shop_api >> README.md
echo    ``` >> README.md
echo 2. Créer et activer un environnement virtuel : >> README.md
echo    ```bash >> README.md
echo    python -m venv venv >> README.md
echo    venv\Scripts\activate >> README.md
echo    ``` >> README.md
echo 3. Installer les dépendances : >> README.md
echo    ```bash >> README.md
echo    pip install -r requirements.txt >> README.md
echo    ``` >> README.md
echo 4. Configurer la base de données PostgreSQL dans `shop_api/settings.py`. >> README.md
echo 5. Appliquer les migrations : >> README.md
echo    ```bash >> README.md
echo    python manage.py migrate >> README.md
echo    ``` >> README.md
echo 6. Créer un superutilisateur : >> README.md
echo    ```bash >> README.md
echo    python manage.py createsuperuser >> README.md
echo    ``` >> README.md
echo 7. Lancer le serveur : >> README.md
echo    ```bash >> README.md
echo    python manage.py runserver >> README.md
echo    ``` >> README.md
echo. >> README.md
echo ## Endpoints API >> README.md
echo - `GET /api/categories/` : Liste des catégories >> README.md
echo - `POST /api/register/` : Inscription d'un utilisateur >> README.md
echo - `GET /api/transactions/` : Liste des transactions >> README.md
echo - (Voir la documentation complète pour tous les endpoints) >> README.md
echo. >> README.md
echo ## Fonctionnalités >> README.md
echo - Gestion des utilisateurs, boutiques, articles, et transactions. >> README.md
echo - Interface d'administration Django pour gérer les données. >> README.md
echo - Validation de la force des mots de passe via l'interface client (showStrength). >> README.md