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
	rm -r bin include lib parts pyvenv.cfg .installed.cfg

bin/instance: bin/buildout

bin/buildout: bin/pip
	bin/pip install -r https://dist.plone.org/release/6.0.6/requirements.txt

bin/pip:
	python3.11 -m venv .
