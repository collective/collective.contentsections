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

bin/instance: bin/buildout

bin/buildout: bin/pip
	bin/pip install -r https://dist.plone.org/release/6.1.0/requirements.txt

bin/pip:
	pyenv local 3.12
	python3.12 -m venv .
