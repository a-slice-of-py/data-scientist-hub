include config.mk

## __LAUNCH_FROM_BASE_ENV__ create-env: initialize python virtual environment
.PHONY: create-env
create-env:
	@echo $(CLIP_MESSAGE)
	@echo "conda create --prefix $(ENV_NAME) python=$(PY_VERSION)" | clip

## activate-env: activate python virtual environment
.PHONY: activate-env
activate-env:
	@echo $(CLIP_MESSAGE)
	@echo "conda-activate $(ENV_NAME)/" | clip

## init-env: initialize miniconda environment installing pip
.PHONY: init-env
init-env:
	@echo $(CLIP_MESSAGE)
	@echo "conda install pip" | clip

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