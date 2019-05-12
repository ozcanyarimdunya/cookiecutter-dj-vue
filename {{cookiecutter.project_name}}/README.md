# {{cookiecutter.project_name}} Project

* [x] Django
* [x] django-rest-framework
* [x] JWT based authentication with django-rest-framework-jwt 
* [x] Vuetify
* [x] nginx (installed on python image)


### Installation

Clone the repository, then

```bash
make install
```

```bash
make
``` 

### Local Development

Create a superuser

```bash
make superuser
```

Open a terminal for backend and type

```bash
make run-backend
```

Open a terminal for frontend and type

```bash
make run-frontend
```

Backend will be served at *http://localhost:8000* and frontend will served at *http://localhost:8080*

### Test

**Backend**

```bash
make test
```

```bash
make coverage
```

### Deployment on docker

```bash
make dockerd
```

Application will be served at *http://ip-of-your-server:8000*
