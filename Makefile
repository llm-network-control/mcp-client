run:
	python main.py

pylint:
	pylint $(shell git ls-files '*.py')

ruff_lint_and_fix:
	ruff check . --fix

ruff:
	make ruff_lint_and_fix

lint:
	make ruff
	make pylint

lint_ci:
	ruff check

test:
	pytest

coverage:
	pytest --cov --cov-report html --cov-fail-under 100

coverage_ci:
	pytest --cov --cov-fail-under 100
