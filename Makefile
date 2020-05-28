SHELL := /bin/bash

start-dev:
	@ echo 'Starting development server >>>>>'
	@ python3 manage.py runserver 0.0.0.0:5000

migrate:
	@ echo 'Making and running migration >>>>>'
	@ python manage.py makemigrations && python manage.py migrate

test:
	@ echo 'Runing Tests >>>'
	@ pytest

test-verbose:
	@ echo 'Runing Tests in verbose mode >>>'
	@ py.test -v -s 

seed-data:
	@ echo 'Seeding Data >>>'
	@ python manage.py loaddata states.json