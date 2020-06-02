# Elite
[![Build Status](https://api.travis-ci.org/habibaudu/Elite.svg?branch=dev)](https://travis-ci.org/habibaudu/Elite)

Elite is a social networking app that encourages devs and youths to build things and show to their world.

## Installing

```sh
    $ git clone https://github.com/habibaudu/Elite.git
    $ cd Elite
    $ pipenv install
    $ git checkout dev
```

* Create a `.env` file and copy/paste the environment variables from the `.env_example` file that's already existent in the root project directory.
* Create a postgreSQL database called `elitedb` using the default `postgres` user and change the value of variable `DB_PASSWORD` in your `.env` file to your `postgres` user's password.
* Run the following commands to make the database migrations.

```sh
    $ make migrate

```

## Running the application

Run the command below to run the application locally.
```sh
  $ make start-dev
  ```


## Running the tests

Run the command below to run the tests for the application.
```sh
  $ python manage.py test
  ```

## Coverage
```
    make coverage
```

## Deployment And Documentation

Details will be available shortly

## Built With

The project has been built with the following technologies so far:

* [Django](https://www.djangoproject.com/) - web framework for building websites using Python
* [Django Rest Framework](https://www.django-rest-framework.org) -  for our APIs.
* [Virtual environment](https://virtualenv.pypa.io/en/stable/) - tool used to create isolated python environments
* [pipenv](https://pipenv-fork.readthedocs.io) - package installer for Python
* [PostgreSQL](https://www.postgresql.org/) - database management system used to persists the application's data.

