.PHONY: help  # List phony targets
help:
	@cat "Makefile" | grep '^.PHONY:' | sed -e "s/^.PHONY:/- make/"

.PHONY: install  # Install development environment
install: bin/buildout
	bin/buildout

.PHONY: start  # Start Zope instance
start: bin/instance
	bin/instance fg

.PHONY: clean  # Clean development environment
clean:
	rm -r bin develop-eggs eggs include lib node_modules parts pyvenv.cfg .installed.cfg .python-version

.PHONY: test  # Run tests
test: bin/pytest
	bin/pytest tests

.PHONY: coverage # Run tests with coverage
coverage: bin/pytest
	bin/pytest --cov=collective.contentsections tests

bin/pytest: bin/buildout
	bin/pip install -r requirements-test.txt

bin/instance: bin/buildout

bin/buildout: bin/pip
	bin/pip install -r requirements.txt

bin/pip:
	python3.12 -m venv .
