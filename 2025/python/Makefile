setup:
	uv sync
.PHONY: setup

fetch:
	uv run -m scripts.fetch_input
.PHONY: fetch

lint:
	uvx isort .
	uvx black .
	uvx ruff format .
.PHONY: lint

mypy:
	uv run mypy .
.PHONY: lint
