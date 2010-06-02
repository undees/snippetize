import os

# Where your to-be-displayed source code lives.
#
base = os.getcwd()

# Apple assigns these colors based on your style slide.
#
styles = {
    'Keyword':41,
    'Name.Class':40,
    'Name.Function':47,
    'Literal':46,
    'Paragraph':387,
    'Commment':45,
    'Operator':41,
}

# Parts of files you wish to extract.
#
snippets = {'bar': ['def bar', 'pass']}
