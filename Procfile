web: gunicorn country_app_project.wsgi 
release: python manage.py makemigrations --noinput && python manage.py migrate --noinput
