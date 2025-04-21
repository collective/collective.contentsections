VENV_FOLDER=.venv

.PHONY: help  # List phony targets
help:
	@cat "Makefile" | grep '^.PHONY:' | sed -e "s/^.PHONY:/- make/"

.PHONY: install  # Install development environment
install: $(VENV_FOLDER)/bin/buildout
	$(VENV_FOLDER)/bin/buildout

.PHONY: start  # Start Zope instance
start: bin/instance
	bin/instance fg

.PHONY: clean  # Clean development environment
clean:
	rm -r $(VENV_FOLDER) bin develop-eggs eggs include lib lib64 node_modules parts pyvenv.cfg .installed.cfg .python-version forest.dot forest.json .tox

.PHONY: test  # Run tests
test: $(VENV_FOLDER)/bin/tox
	$(VENV_FOLDER)/bin/tox -e test

.PHONY: coverage # Run tests with coverage
coverage: $(VENV_FOLDER)/bin/tox
	$(VENV_FOLDER)/bin/tox -e coverage

$(VENV_FOLDER)/bin/tox: $(VENV_FOLDER)/bin/buildout
	$(VENV_FOLDER)/bin/uv pip install -r requirements-test.txt

bin/instance: $(VENV_FOLDER)/bin/buildout
	$(VENV_FOLDER)/bin/buildout

$(VENV_FOLDER)/bin/buildout: $(VENV_FOLDER)/bin/pip
	$(VENV_FOLDER)/bin/uv pip install -r requirements.txt

$(VENV_FOLDER)/bin/pip:
	uv venv --seed -p python3.12
	$(VENV_FOLDER)/bin/pip3.12 install uv
