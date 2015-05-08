# -*- coding: utf-8 -*-

# Ensure backwards compatibility with Python 2
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals)
from builtins import *


def {{cookiecutter.cli_entry_point_function_name }}():
    """ Command-line entry point for {{ cookiecutter.repo_name }} """
    print('{{ cookiecutter.repo_name }} placeholder CLI entry point')


def {{cookiecutter.gui_entry_point_function_name }}():
    """ GUI entry point for {{ cookiecutter.repo_name }} """
    print('{{ cookiecutter.repo_name }} placeholder GUI entry point')


if __name__ == 'main':
    {{ cookiecutter.cli_entry_point_function_name }}()
