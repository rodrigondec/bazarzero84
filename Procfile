release: python manage.py makemigrations
release: python manage.py migrate
web: python bazarzero84/manage.py collectstatic --noinput; gunicorn bazarzero84.wsgi --log-file -