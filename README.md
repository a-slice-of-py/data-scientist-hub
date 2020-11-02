# DataScientistHub

DataScientistHub is a Python package initialized with FireUp!

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install data_scientist_hub in edit mode.

```python
>>> pip install -e . # in the root folder (look for setup.py)
```

## Project tree structure

```python
root/
│
├── .venv-data-scientist-hub/
│
├── cdk-app/
|
├── config/
│
├── dashboard/
|   |
│   ├── assets/
|   |
│   ├── components/
|   |
│   ├── app.py
|   |
│   └── utils.py
│
├── data/
│
├── docker/
|   |
│   └── dashboard/
|       |
│       └── Dockerfile
|
├── docs/
|   |
│   ├── css/
│   |   └── mkdocstrings.css
|   |
│   └── index.md
|
├── notebooks/
│
├── tests/
|
├── data_scientist_hub/
|   |
|   ├── __init__.py
│   │
|   ├── core/
│   |   └── __init__.py
│   │
|   └── utils/
│       └── __init__.py
|
├── .dockerignore
├── .env
├── .gitignore
├── config.mk
├── docker-compoe.yml
├── Makefile
├── mkdocs.yml
├── README.md
├── requirements.txt
└── setup.py
```

## Usage

Install [streamlit](https://docs.streamlit.io/) via `pip` and execute the following in the root folder to run Streamlit sample app (by default on port 8501)

```python
>>> cd ./dashboard
>>> streamlit run app.py
```

## Authors

- **Silvio Lugaro**