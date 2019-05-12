#!/usr/bin/env bash

echo "... Starting nginx"
nginx

echo "... Applying Django migrations"
python manage.py makemigrations
python manage.py migrate

echo "... Creating a default user"
python manage.py default_user

echo "... Applying Django collect static"
python manage.py collectstatic --noinput --clear

echo "... Starting Django"
gunicorn config.wsgi -b 0.0.0.0:8000 --reload