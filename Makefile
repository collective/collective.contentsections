VENV_FOLDER=.venv

ifeq (, $(shell which uv ))
  $(error "[ERROR] The 'uv' command is missing from your PATH. Install it from: https://docs.astral.sh/uv/getting-started/installation/")
endif

.PHONY: help
help: ## Display this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: install
install: $(VENV_FOLDER)/bin/buildout .git/hooks/pre-commit ## Install development environment
	$(VENV_FOLDER)/bin/buildout

.PHONY: start
start: bin/instance .git/hooks/pre-commit ## Start Zope instance
	bin/instance fg

.PHONY: clean
clean: ## Clean development environment
	rm -rf $(VENV_FOLDER) bin .coverage .git/hooks/pre-commit .installed.cfg .tox coverage.xml develop-eggs eggs forest.dot forest.json node_modules parts

.PHONY: meta
meta: ## Update configuration files with plone.meta
	uvx --from plone.meta config-package --branch current --no-commit .

.PHONY: test
test: .venv ## Run tests
	uvx tox -e test

.PHONY: coverage
coverage: .venv ## Run tests and report code coverage
	uvx tox -e coverage

.PHONY: lint
lint: .venv ## Run all code quality and formatting checks
	uvx tox -e lint

.PHONY: i18n
i18n: ## Update locales
	@echo "$(GREEN)==> Updating locales$(RESET)"
	cd src/collective/contentsections/locales && ./update.sh

.PHONY: fullrelease
fullrelease: ## Release package with zest.releaser fullrelease
	uvx --from zest.releaser fullrelease

.venv:
	@echo "Creating virtual environment with uv"
	uv venv

$(VENV_FOLDER)/bin/buildout: .venv
	@echo "Installing requirements with uv pip interface"
	uv pip install -r requirements.txt

bin/instance: $(VENV_FOLDER)/bin/buildout
	@echo "Bootstrapping environment with buildout"
	$(VENV_FOLDER)/bin/buildout

.git/hooks/pre-commit: .venv
	@echo "Installing pre-commit hooks"
	uvx pre-commit install
