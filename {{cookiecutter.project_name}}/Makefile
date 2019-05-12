.PHONY: all

all:
	cd frontend && npm run build
	python manage.py collectstatic --noinput --clear
	python manage.py makemigrations
	python manage.py migrate
	python manage.py default_user

build-frontend:
	cd frontend && npm run build

coverage:
	coverage run --source='.' manage.py test apps
	coverage report -m

coverage-html:
	coverage html

dockerd:
	docker-compose up -d --build

install:
	pip install -r requirements.txt
	cd frontend && npm install

migrations:
	python manage.py makemigrations
	python manage.py migrate

run-backend:
	python manage.py runserver

run-frontend:
	cd frontend && npm run serve

superuser:
	python manage.py default_user

test:
	python manage.py test apps