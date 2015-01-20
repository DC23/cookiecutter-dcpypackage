SHELL=/bin/sh

.SILENT:
.IGNORE:

.PHONY: help
help:
	echo
	echo 'Utility Makefile for {{ cookiecutter.project_name }}'
	echo '============================'
	echo
	echo 'Targets supported are:'
	echo
	echo '  * clean: removes the build and htmlcov (coverage reports) directories, as well as __pycache__ and *.pyc files. Note that a clean also removes the generated documentation (as this is placed into build/docs).'
	echo '  * install-deps: installs development and test dependencies into your virtual environment.'
	echo '  * develop: installs {{ cookiecutter.repo_name }} in development mode.'
	echo '  * lint: runs pylint.'
	echo '  * html: builds the HTML documentation.'
	echo '  * pdf: builds the documentation in PDF format.'
	echo '  * latex: builds LaTeX source, used to generate other formats.'
	echo '  * alldocs: builds all documentation formats.'
	echo '  * sdist: builds a source distribution.'
	echo '  * bdist_wheel: builds a universal wheel distribution.'

.PHONY: test
test:
	py.test

.PHONY: tests
tests: test

.PHONY: clean
clean:
	rm -rf build/ htmlcov/
	find ./src/ -name "__pycache__" -exec rm -rf {} \;
	find ./src/ -name "*.pyc" -exec rm -rf {} \;

.PHONY: install-deps
install-deps:
	pip install --upgrade -e.[dev,test]

develop: install-deps
	python setup.py develop

.PHONY: lint
lint:
	pylint ./src/{{ cookiecutter.repo_name }}/

.PHONY: sdist
sdist:
	python setup.py sdist

.PHONY: bdist_wheel
bdist_wheel:
	python setup.py bdist_wheel

.PHONY: html
html:
	sphinx-build -b html docs build/docs/html

.PHONY: latex
latex:
	sphinx-build -b latex docs build/docs/latex

pdf: latex 
	$(MAKE) -C build/docs/latex all-pdf
	mkdir -p ./build/docs/pdf/
	mv build/docs/latex/*.pdf build/docs/pdf/

alldocs: html latex pdf

