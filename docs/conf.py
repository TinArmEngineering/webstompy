# -*- coding: utf-8 -*-
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

from webstompy.version import __version__

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'webstompy'
copyright = 'Point 8 GmbH'
author = 'Point 8 GmbH'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'{}'.format(__version__)
# The full version, including alpha/beta/rc tags.
release = u'{}'.format(__version__)

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for napoleon extension ---------------------------------------
# see: http://www.sphinx-doc.org/en/stable/ext/napoleon.html

napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

# -- Options for intersphinx extension ---------------------------------------
# see: http://www.sphinx-doc.org/en/stable/ext/intersphinx.html

intersphinx_mapping = {'python': ('https://docs.python.org/3.5', None),
                       'numpy': ('http://docs.scipy.org/doc/numpy/', None),
                       'sklearn': ('http://scikit-learn.org/stable', None)}

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'webstompy'