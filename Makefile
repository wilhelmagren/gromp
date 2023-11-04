.PHONY: clean
clean:
	poetry run pyclean gromp tests

.PHONY: install
install:
	poetry install --with dev --no-root

.PHONY: test
test:
	poetry run pytest tests

.PHONY: format
format:
	poetry run black gromp tests

.PHONY: lint
lint:
	poetry run ruff check gromp tests --fix

.PHONY: clean-test
clean-test: clean test
