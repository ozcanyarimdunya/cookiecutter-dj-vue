Cookiecutter django/django-rest-framework with vue/vuetify
===========================================================

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter)

## Features

1. Docker
2. Backend: django + django-rest-framework
3. Frontend: vue + vuetify
4. Database: sqlite3(local) + postgresql(production)
5. Server: Nginx
6. Authentication: JWT authentication


## Usage

First, get cookiecutter:

	$ pip install cookiecutter

Now run it against this repo:

	$ cookiecutter gh:ozcanyarimdunya/cookiecutter-dj-vue

You'll be prompted only for project name. Provide it, then a project will be created for you. 

Now you can start project with docker-compose:

	$ docker-compose up -d --build

