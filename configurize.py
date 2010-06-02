#!/usr/bin/env python

from xml.dom import minidom
from zipfile import ZipFile
import re
import sys
import xpath

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        sys.stderr.write('Usage: snippetize IN.key > CONFIG.py\n')
        exit(-1)

    key_file = sys.argv[1]

    zf = ZipFile(key_file)
    raw = zf.read('index.apxl')
    doc = minidom.parseString(raw)
    slide_path = '//sf:shape[@sf:href=\'http://localhost:8081/style\']'
    slide = xpath.find(slide_path, doc)[0]
    body = slide.getElementsByTagName('sf:text-body')[0]

    patterns = {
        'Paragraph':'sf:p[contains(text(),\'value\')]',
        'Keyword':'sf:p/sf:span[contains(text(),\'def\')]',
        'Operator':'sf:p/sf:span[contains(text(),\'=\')]',
        'Commment':'sf:p/sf:span[contains(text(),\'# \')]',
        'Literal':'sf:p/sf:span[contains(text(),\'Lit\')]',
        'Name.Function':'sf:p/sf:span[contains(text(),\'meth\')]',
        'Name.Class':'sf:p/sf:span[contains(text(),\'Cls\')]',
        }

    print 'styles = {'

    for key in patterns:
        pattern = patterns[key]
        node = xpath.find(pattern, body)[0]
        style = node.getAttribute('sf:style')
        number = re.search('(\d+)$', style).groups()[0]
        print "    '%s':%s," % (key, number)

    print '}'
