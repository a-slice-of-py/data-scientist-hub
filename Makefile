include config.mk

## __LAUNCH_FROM_BASE_ENV__ create-env: initialize python virtual enviroment
.PHONY: create-env
create-env:
	virtualenv $(ENV_NAME)

## activate-env: activate python virtual enviroment
.PHONY: activate-env
activate-env:
	@echo "Command stored! You can past and run it in the CLI."
	@echo "$(ENV_NAME)\Scripts\activate.bat" | clip

## init: initialize package basic dependencies
.PHONY: init
init:
	$(PYTHON) -m pip install -r ./requirements.txt

## register-env: register virtual enviroment in jupyter suite
.PHONY: register-env
register-env:
	$(PYTHON) -m ipykernel install --user --name=$(ENV_NAME)

## reqs: save requirements.txt with pipreqs
.PHONY: reqs
reqs:
	pipreqs ./ --encoding latin --ignore $(ENV_NAME)

## install-package: install python package in edit mode
.PHONY: install-package
install-package:
	$(PYTHON) -m pip install -e .

## streamlit-run: run streamlit app
.PHONY: streamlit-run
streamlit-run:
	cd ./dashboard && streamlit run app.py

## docs-serve: serve package docs on localhost
.PHONY: docs-serve
docs-serve:
	mkdocs serve

## docs-build: build package docs as static html website
.PHONY: docs-build
docs-build:
	mkdocs build --no-directory-urls

## test: execute tests with pytest and dump html report
.PHONY: test
test:
	cd tests && $(PYTHON) test_loguru.py && pytest --html=pytest-report.html

.PHONY: help
help: Makefile
	@sed -n 's/^## //p' $<