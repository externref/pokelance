import os
import sys

sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("../"))

project = "discmon"
copyright = "2022, sarthak-py"
author = "sarthak-py"

release = "0.1.0-alpha"

extensions = [
    "myst_parser",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.coverage",
]

templates_path = ["_templates"]

exclude_patterns = []
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
source_suffix = [".rst", ".md"]
