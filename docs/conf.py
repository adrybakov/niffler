import sys
from datetime import datetime
from os.path import abspath

version = "0.0.0"

sys.path.insert(0, abspath("."))


##########################################################################################
##                                   Project metadata                                   ##
##########################################################################################
project = "Niffler"
copyright = f"2024-{datetime.now().year}, Niffler Team"
author = "Niffler Team"


##########################################################################################
##                                      Extensions                                      ##
##########################################################################################
extensions = [
    "sphinx.ext.duration",  # Measure the time of the build
    "sphinx.ext.autodoc",  # Pull documentation from the docstrings
    "sphinx.ext.autosummary",  # Generate autodoc summaries
    "sphinx.ext.viewcode",  # Add links to highlighted source code
    "sphinx.ext.extlinks",  # Markup to shorten external links
    "sphinx.ext.intersphinx",  # Link to other projects’ documentation
    "sphinx.ext.doctest",  # For the doctests
    "sphinx.ext.mathjax",  # For latex-style math
    "sphinx_copybutton",  # Copybutton for the blocks
    "sphinx_design",  # For the design elements on the from page
    "numpydoc",  # For the numpy-style docstrings
]


##########################################################################################
##                                  Build configuration                                 ##
##########################################################################################
autosummary_generate = True
autodoc_member_order = "alphabetical"
smartquotes = False

# Avoid double generating the entries for the members of the class
numpydoc_class_members_toctree = False

# Fix problem with autosummary and numpydoc:
numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]


##########################################################################################
##                                Options for HTML output                               ##
##########################################################################################

html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["niffler.css"]

html_title = f"{project} {version}"

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#198F88",
        "color-code-background": "#E6E6E6",
    },
    "dark_css_variables": {
        "color-brand-primary": "#7BC4AC",
    },
    "source_repository": "https://github.com/adrybakov/niffler",
    "source_branch": "main",
    "source_directory": "docs/",
    "top_of_page_button": "edit",
    "navigation_with_keys": True,
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/adrybakov/niffler",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}


##########################################################################################
##              Custom variables with access from .rst files and docstrings             ##
##########################################################################################
variables_to_export = [
    "project",
    "copyright",
    "version",
]

frozen_locals = dict(locals())
rst_epilog = "\n".join(
    map(lambda x: f".. |{x}| replace:: {frozen_locals[x]}", variables_to_export)
)
del frozen_locals


##########################################################################################
##                                Dynamic external links                                ##
##########################################################################################
# Usage :issue:`123`
extlinks = {
    "DOI": ("https://doi.org/%s", "DOI: %s"),
    "issue": ("https://github.com/adrybakov/niffler/issues/%s", "issue #%s"),
}


##########################################################################################
##                                 Static external links                                ##
##########################################################################################

# Solution source:
# https://docutils.sourceforge.io/docs/ref/rst/directives.html#directives-for-substitution-definitions
# Usage: |Python|_
custom_links = {
    "Python": ("Python", "https://python.org"),
}


rst_epilog += "\n".join(
    map(
        lambda x: f"\n.. |{x}| replace:: {custom_links[x][0]}\n.. _{x}: {custom_links[x][1]}",
        [i for i in custom_links],
    )
)