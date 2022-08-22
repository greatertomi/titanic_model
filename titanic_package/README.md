# Titanic AI Model Package

This package uses [tox](https://tox.wiki/en/latest/) for automation. Install tox before running this project.

## Commands

- `tox -e test_package` to run tests
- `tox -e train` to train model
- `tox -e lint` run linter through the code
- `tox -e stylechecks` to run the style checker

## Build

To create a distributable build

- `python3 -m pip install --upgrade build` to install build script
- `python3 -m build` to build.

The file would be located in the `dist` folder.

Look [here](https://packaging.python.org/en/latest/tutorials/installing-packages/) to learn more about packaging
