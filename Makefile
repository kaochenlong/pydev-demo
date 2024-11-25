.PHONY: server
server:
	poetry run python manage.py runserver

.PHONY: migrate
migrate:
	poetry run python manage.py migrate
