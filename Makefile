lint:
	poetry run flake8


test-coverage:
	poetry run coverage run --source=gendiff -m pytest tests
	poetry run coverage report -m
	poetry run coveralls

