release: python manage.py makemigrations
release: python manage.py migrate
web: python manage.py collectstatic --noinput; gunicorn bazarzero84.wsgi --log-file -