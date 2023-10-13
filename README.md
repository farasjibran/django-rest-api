<div align="center">

# Todo API

![Python version](https://img.shields.io/badge/Pythn-3.8.10-4c566a?logo=python&&longCache=true&logoColor=white&colorB=pink&style=flat-square&colorA=4c566a) ![Django version](https://img.shields.io/badge/Django-4.2.6-4c566a?logo=django&&longCache=truelogoColor=white&colorB=pink&style=flat-square&colorA=4c566a) ![Django-RestFramework](https://img.shields.io/badge/Django_Rest_Framework-0.1.0-red.svg?longCache=true&style=flat-square&logo=django&logoColor=white&colorA=4c566a&colorB=pink) ![Stars](https://img.shields.io/github/forks/Ceci-Aguilera/truck_signs_frontend?&&longCache=true&logoColor=white&colorB=yellow&style=flat-square&colorA=4c566a) ![Forks](https://img.shields.io/github/stars/Ceci-Aguilera/truck_signs_api?&&longCache=true&logoColor=white&colorB=yellow&style=flat-square&colorA=4c566a) ![Commit activity](https://img.shields.io/github/commit-activity/y/Ceci-Aguilera/truck_signs_api/master?&&longCache=true&logoColor=white&colorB=green&style=flat-square&colorA=4c566a)

</div>

## Table of Contents

- [Description](#intro)
- [Install (Run) with Docker](#docker)
- [Installation without Docker](#installation)
- [Useful Links](#useful_links)

<a name="intro"></a>

## Description

**Todo API** is an project for me to learn how to use the django in python and how to dockerize the project

<a name="docker"></a>

## Install (Run) with Docker

### About the Builds and Images in use:

There are currently 3 services in use: the api (Django App), the db (the postgrSQL database), and the nginx (Nginx configuration). - **api:** The Django Dockerfile is in the root directory, and it has an entrypoint file that connects the backend to the database and runs migrations as well as collects the statics. - **db:** This is built from the postgres:13-alpine image. The default environment variables are set in the docker-compose.yml file. - **nginx:** The default configuration for nginx is inside the nginx folder in the nginx.conf file.

### Runing Docker-Compose

1. Clone the repo:
   ```bash
   git clone https://github.com/farasjibran/django-rest-api
   ```
1. Configure the environment variables.

   1. Copy the content of the example env file that is inside the django-rest-api folder into a .env file:
      ```bash
      cp .env.example .env
      ```
   1. The new .env file should contain all the environment variables necessary to run all the django app in all the environments. However, the only needed variables for docker to run are the following:
      ```bash
      SECRET_KEY
      DB_NAME
      DB_USER
      DB_PASSWORD
      DB_HOST
      DB_PORT
      ```
   1. For the database, the default configurations should be:
      ```bash
      DB_NAME=db_todos
      DB_USER=todos_user
      DB_PASSWORD=todos_password!
      DB_HOST=db
      DB_PORT=5432
      ```
   1. The DOCKER_SECRET_KEY is the django secret key. To generate a new one see: [Stackoverflow Link](https://stackoverflow.com/questions/41298963/is-there-a-function-for-generating-settings-secret-key-in-django)

1. Run docker-compose:
   ```bash
   docker-compose up --build
   ```
1. Congratulations =) !!! The App should be running in [localhost:80](http://localhost:80)
1. (Optional step) To create a super user run:
   ```bash
   docker-compose run api ./manage.py createsuperuser
   ```

<a name="installation"></a>

## Installation without Docker

1. Clone the repo:
   ```bash
   git clone https://github.com/farasjibran/django-rest-api
   ```
1. Configure a virtual env and set up the database. See [Link for configuring Virtual Environment](https://docs.python-guide.org/dev/virtualenvs/) and [Link for Database setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04).
1. Configure the environment variables.

   1. Copy the content of the example env file that is inside the django-rest-api folder into a .env file:
      ```bash
      cp .env.example .env
      ```
   1. The new .env file should contain all the environment variables necessary to run all the django app in all the environments. However, the only needed variables for the development environment to run are the following:
      ```bash
      SECRET_KEY
      DB_NAME
      DB_USER
      DB_PASSWORD
      DB_HOST
      DB_PORT
      ```
   1. For the database, the default configurations should be:
      ```bash
      DB_NAME=todo_app
      DB_USER=postgres
      DB_PASSWORD=
      DB_HOST=localhost
      DB_PORT=5432
      ```
   1. The SECRET_KEY is the django secret key. To generate a new one see: [Stackoverflow Link](https://stackoverflow.com/questions/41298963/is-there-a-function-for-generating-settings-secret-key-in-django)

1. Run the migrations and then the app:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
1. Congratulations =) !!! The App should be running in [localhost:8000](http://localhost:8000)
1. (Optional step) To create a super user run:
   ```bash
   python manage.py createsuperuser
   ```

<a name="useful_links"></a>

## Useful Links

### Postgresql Databse

- Setup Database: [Digital Ocean Link for Django Deployment on VPS](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)

### Docker

- [Docker Oficial Documentation](https://docs.docker.com/)
- Dockerizing Django, PostgreSQL, guinicorn, and Nginx:
  - Github repo of sunilale0: [Link](https://github.com/sunilale0/django-postgresql-gunicorn-nginx-dockerized/blob/master/README.md#nginx)
  - My repo to Dockerize Django + Postgresql + Nginx + React js: [Ceci-Aguilera/django-react-nginx-mysql-docker](https://github.com/Ceci-Aguilera/django-react-nginx-mysql-docker)
  - Michael Herman article on testdriven.io: [Link](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)

### Django and DRF

- [Django Official Documentation](https://docs.djangoproject.com/en/4.0/)
- Generate a new secret key: [Stackoverflow Link](https://stackoverflow.com/questions/41298963/is-there-a-function-for-generating-settings-secret-key-in-django)
- Modify the Django Admin:
  - Small modifications (add searching, columns, ...): [Link](https://realpython.com/customize-django-admin-python/)
  - Modify Templates and css: [Link from Medium](https://medium.com/@brianmayrose/django-step-9-180d04a4152c)
- [Django Rest Framework Official Documentation](https://www.django-rest-framework.org/)
- More about Nested Serializers: [Stackoverflow Link](https://stackoverflow.com/questions/51182823/django-rest-framework-nested-serializers)
- More about GenericViews: [Testdriver.io Link](https://testdriven.io/blog/drf-views-part-2/)

### Miscellaneous

- Create Virual Environment with Virtualenv and Virtualenvwrapper: [Link](https://docs.python-guide.org/dev/virtualenvs/)
- [Configure CORS](https://www.stackhawk.com/blog/django-cors-guide/)
- [Setup Django with Cloudinary](https://cloudinary.com/documentation/django_integration)
