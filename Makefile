SHELL := /bin/bash

start-dev:
	@ echo 'Starting development server >>>>>'
	@ python3 manage.py runserver 0.0.0.0:5000

migrate:
	@ echo 'Making and running migration >>>>>'
	@ python3 manage.py makemigrations && python3 manage.py migrate