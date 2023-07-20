# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'G-NAF'
copyright = '2023, Geoscape'
author = 'Geoscape'

release = 'May'
version = '2023'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Option for PDF ouput
latex_elements = { 'papersize' : 'a4paper' ,
                'preamble': r'''\usepackage{lscape}''',
                   'extrapackages' :'''\\usepackage {titlesec} \\titleformat {\\chapter}[display] {\\normalfont\\bfseries}{} {0 pt}{\\Huge}''' }


# -- Options for EPUB output
epub_show_urls = 'footnote'
