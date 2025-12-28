.PHONY: build run

build:
	uv run ruff check --show-fixes --fix src/.
	uv run ruff format src/.
	uv run mypy src/.

run: build
	uv run src/main.py
