cookiecutter-dcpypackage
========================

A [cookiecutter](https://github.com/audreyr/cookiecutter) template, with
the author's preferred Python package setup.

Features:

* utility makefile for common tasks.
* [pytest](http://pytest.org/latest/) for unit tests, with integration into setup.py.
    * [pytest-cov](https://pypi.python.org/pypi/pytest-cov) plugin for test coverage reporting.
    * [pytest-sugar](https://pypi.python.org/pypi/pytest-sugar) plugin for pretty test output.
    * HTML coverage reports are enabled by default. See the htmlcov directory.
* [pylint](http://docs.pylint.org), with tests excluded by default.
* [sphinx](http://sphinx-doc.org/index.html) documentation, with shared files between Sphinx and the Python package files, for reduced maintenance.
* [bumpversion](https://pypi.python.org/pypi/bumpversion) for version management
* Universal build, targetting Python 2 and 3.
* Most build artifacts go to a common build directory.

Inspiration, and some boilerplate text taken from some other templates,
including:

* [cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
* [cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary)

Usage
-----
Install cookiecutter if you haven't already. Then, create a project in
your current working directory using:

    $ cookiecutter gh:DC23/cookiecutter-dcpypackage

Once your project is created, the next steps should be to create a
virtual environment (using either virtualenv/virtualenvwrapper or the
virtual environment functionality built into Python 3):

    $ mkvirtualenv -a . my_project

With the virtual environment activated, install the initial development
dependencies including installing your package in development mode:

    $ make develop

After that, you can start customising the templates to suit your needs.
Run make with no target for a list of make options:

    $ make

Note that bumpversion does not have a make target. It is easier to run
bumpversion directly.
