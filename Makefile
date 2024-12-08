# Variables
PYTHON = python
PIP = pip
FLASK_APP = app.py
FLASK_ENV = development
FLASK_PORT = 3000
VENV = .venv

# Default target
.PHONY: all
all: install run

# Create a virtual environment
.PHONY: venv
venv:
	$(PYTHON) -m venv $(VENV)

# Install dependencies
.PHONY: install
install: venv
	$(VENV)/bin/$(PIP) install -r requirements.txt

# Run the Flask app
.PHONY: run
run:
	FLASK_APP=$(FLASK_APP) FLASK_ENV=$(FLASK_ENV) $(VENV)/bin/flask run --port=$(FLASK_PORT)

# Clean up generated files
.PHONY: clean
clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Lint the Python code
.PHONY: lint
lint:
	$(VENV)/bin/$(PIP) install flake8
	$(VENV)/bin/flake8 .

# Run tests (if any)
.PHONY: test
test:
	$(VENV)/bin/$(PYTHON) -m unittest discover -s tests