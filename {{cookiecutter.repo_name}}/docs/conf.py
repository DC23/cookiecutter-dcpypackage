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
project = u'Sambuca'
copyright = u'2014-15, CSIRO'
version = release = '0.1.0'
pygments_style = 'trac'
templates_path = ['.']
html_theme = 'default'
html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = True
html_sidebars = {
   '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)
html_theme_options = {
    # TODO: real project url
    # 'githuburl': 'https://github.com/dc23/sambuca/'
}
