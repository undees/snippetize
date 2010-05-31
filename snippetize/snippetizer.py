from __future__ import with_statement
from os.path import join, expanduser
from keynote_formatter import KeynoteFormatter
from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from shutil import copyfile
from snippetize.extractor import Extractor
from snippetize.finder import Finder
from snippetize.replacer import Replacer
from xml.dom import minidom
from zipfile import ZipFile
import codecs
import snippetize.core_ext

class Snippetizer:
    def __init__(self, keynote_file, config_file):
        config = {}
        execfile(config_file, config)
        self.base = config['base']
        self.extractor = Extractor(config['snippets'])
        self.formatter = KeynoteFormatter(config['styles'])

    def snippetize(self):
        with ZipFile('all.key') as original:
            with ZipFile('out.key', 'w') as updated:
                for item in original.filelist:
                    if item.filename != 'index.apxl':
                        contents = original.read(item.filename)
                        updated.writestr(item, contents)
            raw = original.read('index.apxl')


        doc = minidom.parseString(raw)
        pattern = '//sf:shape[starts-with(@sf:href,\'http://localhost/\')]'
        strip = 'http://localhost/'
        finder = Finder(doc, pattern, strip)

        template = '''<?xml version="1.0"?>
<key:presentation
     xmlns:sfa="http://developer.apple.com/namespaces/sfa"
     xmlns:sf="http://developer.apple.com/namespaces/sf"
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xmlns:key="http://developer.apple.com/namespaces/keynote2">
  <sf:text-body>
    %s
  </sf:text-body>
</key:presentation>
'''

        replacer = Replacer(doc, template)

        names = finder.snippets()
        for name in names:
            filename, _, part = name.partition('?')
            path = expanduser(join(self.base, filename))
            with open(path) as file:
                code = self.extractor.extract(file.read(), part)
            lexer = get_lexer_for_filename(filename, stripall=True)
            snippet = highlight(code, lexer, self.formatter)

            parent = '//sf:shape[@sf:href="http://localhost/%s"]//sf:text-storage' % name
            child = 'sf:text-body'
            replacer.replace(parent, child, snippet)

        with ZipFile('out.key', 'a') as updated:
            updated.writestr('index.apxl', doc.toxml().encode('utf-8'))
