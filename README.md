# Demo for a shared library

Common code will be shared and reused by multiple projects inside the company.

The goal is to package that common code as a classical python library, save it to Azure Artifacts and make it available to other projects.

## Running tests

To run tests:
```
pytest
```

## Creating the distribution

To create the distribution:
```
python setup.py sdist bdist_wheel
```
