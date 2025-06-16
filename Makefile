ifeq (, $(shell which uv ))
  $(error "[ERROR] The 'uv' command is missing from your PATH. Install it from: https://docs.astral.sh/uv/getting-started/installation/")
endif

.PHONY: help
help: ## Display this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: bootstrap
bootstrap: .venv/bin/buildout ## Bootstrap the development environment

.PHONY: install
install: .venv/bin/buildout ## Install Plone
	.venv/bin/buildout

.PHONY: start
start: bin/instance ## Start Zope instance
	bin/instance fg

.PHONY: clean
clean: ## Clean development environment
	rm -rf .venv bin .coverage .git/hooks/pre-commit .installed.cfg .tox coverage.xml develop-eggs eggs forest.dot forest.json node_modules parts

.PHONY: meta
meta: ## Update configuration files with plone.meta
	uvx --from plone.meta config-package --branch current --no-commit .

.PHONY: test
test: ## Run tests
	uvx tox -e test

.PHONY: coverage
coverage: ## Run tests and report code coverage
	uvx tox -e coverage

.PHONY: lint
lint: ## Run all code quality and formatting checks
	uvx tox -e lint

.PHONY: i18n
i18n: ## Update locales
	@echo "$(GREEN)==> Updating locales$(RESET)"
	cd src/collective/contentsections/locales && ./update.sh

.PHONY: fullrelease
fullrelease: ## Release package with zest.releaser fullrelease
	uvx --from zest.releaser fullrelease

.venv/bin/buildout:
	uv venv
	uv pip install -r requirements.txt
	uvx pre-commit install

bin/instance: .venv/bin/buildout
	.venv/bin/buildout
