from xml.dom import minidom
import xpath

class Replacer:
    """Replaces code snippets in an XML document."""

    def __init__(self, doc, template):
        """Stores a parsed XML document and replacement template.
        Templates should contain a %s, like so:
        <document>%s</document>"""

        self.doc = doc
        self.template = template

    def replace(self, parent, child, snippet):
        """Replaces a parent's child (both given as XPath) with
        a snippet of raw XML."""

        parent_node = xpath.find(parent, self.doc)[0]
        child_node  = parent_node.getElementsByTagName(child)[0]
        new_content = self.template % snippet
        new_xml     = minidom.parseString(new_content)
        new_node    = new_xml.getElementsByTagName(child)[0]

        parent_node.removeChild(child_node)
        parent_node.appendChild(new_node)
