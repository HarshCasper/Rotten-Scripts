# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Rotten Scripts'
copyright = '2021, Harsh Bardhan Sharma'
author = 'Avinal Kumar'

# The full version, including alpha/beta/rc tags
release = "1.0.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_copybutton'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['./templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
html_logo = "assets/banner.png"
html_title = "Rotten Scripts"
html_copy_source = True
html_sourcelink_suffix = ""
html_favicon = "assets/banner.png"
html_last_updated_fmt = ""

html_theme_options = {
    "theme_dev_mode": True,
    "use_edit_page_button": True,
    "repository_url": "https://github.com/HarshCasper/Rotten-Scripts",
    "repository_branch": "master",
    "use_issues_button": True,
    "use_repository_button": True,
}

html_baseurl = "https://HarshCasper.github.io/rotten-scripts"
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['./assets']