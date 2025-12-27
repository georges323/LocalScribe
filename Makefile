.PHONY: build run

build:
	uv run ruff check --show-fixes --fix .
	uv run ruff format .
	uv run mypy .

run: build
	uv run main.py
