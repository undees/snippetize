from snippetize.replacer import Replacer
from xml.dom import minidom
import xpath

def test_replacer():
    doc = minidom.parse('index.apxl')
    template = '''<?xml version="1.0"?>
<key:presentation
     xmlns:sfa="http://developer.apple.com/namespaces/sfa"
     xmlns:sf="http://developer.apple.com/namespaces/sf"
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xmlns:key="http://developer.apple.com/namespaces/keynote2">
  %s
</key:presentation>
'''

    replacer = Replacer(doc, template)
    parent   = '//sf:shape[@sf:href="http://localhost/all.rb"]//sf:text-storage'
    child    = 'sf:text-body'
    snippet  = '<sf:text-body><sf:p sf:style="SFWPParagraphStyle-373"># Comment<sf:br/></sf:p></sf:text-body>'

    replacer.replace(parent, child, snippet)

    tags   = xpath.find(parent, replacer.doc)[0].toprettyxml()
    lines  = [line.strip() for line in tags.splitlines()]
    lines  = [line for line in lines if len(line) > 0]
    actual = '\n'.join(lines)

    expected = '''<sf:text-storage sf:excl="G" sf:kind="textbox" sfa:ID="SFWPStorage-2">
<sf:stylesheet-ref sfa:IDREF="SFSStylesheet-15"/>
<sf:text-body>
<sf:p sf:style="SFWPParagraphStyle-373">
# Comment
<sf:br/>
</sf:p>
</sf:text-body>
</sf:text-storage>'''

    assert(actual == expected)
