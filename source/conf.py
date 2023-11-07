# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = ""
copyright = "CC BY-ND 4.0 DEED"
author = 'cronologic GmbH & Co. KG'
# release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "tbt2pcie": (
        "https://ug-hub.readthedocs.io/projects/tbt2pcie/en/latest/",
        None
    )
}
intersphinx_disabled_reftypes = ["*"]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
# html_extra_path = ["_404"]
