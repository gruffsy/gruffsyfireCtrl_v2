python manage.py collectstatic --noinput
    python manage.py makemigrations    
    python manage.py migrate
    python manage.py runserver --settings=backend.settings.prod