run:
	python manage.py runserver

migrate:
	python manage.py makemigrations && python manage.py migrate

.DEFAULT_GOAL: run