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
test: bin/tox
	bin/tox -e test

.PHONY: coverage # Run tests with coverage
coverage: bin/tox
	bin/tox -e coverage

.PHONY: lint # Run tests with lint
lint: bin/tox
	bin/tox -e lint

# i18n
$(VENV_FOLDER)/bin/i18ndude: $(VENV_FOLDER)/bin/pip
	@echo "$(GREEN)==> Install translation tools$(RESET)"
	$(VENV_FOLDER)/bin/uv pip install i18ndude

.PHONY: i18n # Update locales
i18n: bin/i18ndude
	@echo "$(GREEN)==> Updating locales$(RESET)"
	cd src/collective/contentsections/locales && ./update.sh


# bin/tox: $(VENV_FOLDER)/bin/buildout
# 	$(VENV_FOLDER)/bin/uv pip install -r requirements-test.txt

bin/instance: $(VENV_FOLDER)/bin/buildout
	$(VENV_FOLDER)/bin/buildout

$(VENV_FOLDER)/bin/buildout: $(VENV_FOLDER)/bin/pip
	$(VENV_FOLDER)/bin/uv pip install -r requirements.txt

$(VENV_FOLDER)/bin/pip:
	uv venv --seed -p python3.12
	$(VENV_FOLDER)/bin/pip3.12 install uv
