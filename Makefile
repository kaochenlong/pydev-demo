.PHONY: server
server:
	poetry run python manage.py runserver

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: shell
shell:
	poetry run python manage.py shell_plus

.PHONY: precommit
precommit:
	poetry run pre-commit

.PHONY: commit
commit:
	poetry run cz commit
