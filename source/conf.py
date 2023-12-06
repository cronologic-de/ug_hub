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

html_theme = "alabaster"
html_static_path = ["_static"]
html_favicon = "_static/cronologic_favicon.svg"
html_sidebars = {
    '**': [
        'about.html',
        "navigation.html",
    ]
}
html_theme_options = {
    "font_family" : "Montserrat, sans-serif",
    "sidebar_collapse": False,
    "extra_nav_links": {
        "Homepage": "https://www.cronologic.de/",
        "Imprint": "https://www.cronologic.de/contact"
    },
    "fixed_sidebar": True,
    "logo": "cronologic.svg",
    "description": f"GmbH & Co. KG",
    "show_powered_by": False,
    # colors
    "body_text" : "#737372",
    "link_hover": "#376EB5",
}
