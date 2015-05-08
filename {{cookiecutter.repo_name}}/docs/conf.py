# -*- coding: utf-8 -*-
import os

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    # 'sphinx.ext.napoleon', # required when sphinx moves to version >=1.3
    'sphinxcontrib.napoleon',
]
if os.getenv('SPELLCHECK'):
    extensions += 'sphinxcontrib.spelling',
    spelling_show_suggestions = True
    spelling_lang = 'en_US'

source_suffix = '.rst'
master_doc = 'index'
project = '{{ cookiecutter.project_name }}'
copyright = '{{ cookiecutter.year }}, {{ cookiecutter.organisation }}'
version = release = '{{ cookiecutter.version }}'
pygments_style = 'trac'
templates_path = ['.']
html_theme = 'alabaster'
html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = True
html_sidebars = {
   '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)
html_theme_options = {
    #'githuburl': 'https://github.com/dc23/sambuca/'
}
