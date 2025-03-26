# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------
project = u"pdf_utility"
copyright = u"2025, Oluwafemi Omitusa"
author = u"Oluwafemi Omitusa"
version = "0.1.0"
release = version

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_nb",
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "sphinx_rtd_theme",
]

# Autoapi settings
autoapi_dirs = ["../src"]
autoapi_type = 'python'
autoapi_template_dir = '_templates'
autoapi_generate_api_docs = True
autoapi_add_toctree_entry = True

# MyST settings
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
nb_execution_mode = "off"

# Napoleon settings
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_type_aliases = None

# Theme settings
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_nav_header_background': '#2980B9',
}

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# List of patterns to ignore when building the documentation
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
