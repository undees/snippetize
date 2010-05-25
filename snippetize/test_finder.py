from __future__ import with_statement
from snippetize.finder import Finder
from xml.dom import minidom
from zipfile import ZipFile
import codecs
import snippetize.core_ext
import xpath

def test_finder():
    with ZipFile('all.key') as file:
        raw = file.read('index.apxl')

    doc = minidom.parseString(raw)
    pattern = '//sf:shape[starts-with(@sf:href,\'http://localhost/\')]'
    strip = 'http://localhost/'
    finder = Finder(doc, pattern, strip)

    actual = finder.snippets()
    expected = ['example.py?bar']
    assert(actual == expected)
