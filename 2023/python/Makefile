setup:
	[ -d venv ] || python -m venv venv
	source venv/bin/activate && pip install -r requirements.txt
.PHONY: setup

fetch:
	source venv/bin/activate && python -m scripts.fetch_input
.PHONY: fetch

lint:
	python -m black .
.PHONY: lint

mypy:
	python -m mypy .
.PHONY: lint
