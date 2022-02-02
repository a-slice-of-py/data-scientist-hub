# Pre-commit hooks

```yaml title=".pre-commit-config.yaml"
repos:
  - repo: https://github.com/pre-commit/mirrors-autopep8
    rev: v1.6.0
    hooks:
      - id: autopep8
        name: Format code according to PEP 8
        types: [python]
  - repo: https://github.com/myint/docformatter
    rev: v1.4
    hooks:
      - id: docformatter
        name: Format docs according to PEP 257
        types: [python]
  - repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort
        name: Sort imports
        types: [python]
```