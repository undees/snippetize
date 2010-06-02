import xpath

class Finder:
    '''Finds places in an XML document to insert code snippets.'''

    def __init__(self, doc, pattern, strip):
        '''Stores a parsed DOM document, an XPath expression to
        search for, and text to strip from the resulting value.'''

        self.doc     = doc
        self.pattern = pattern
        self.strip   = strip

    def snippets(self):
        '''Searches through the DOM document for all nodes
        matching self.pattern.  Takes the href attribute
        from each node, and strips out occurrences of self.strip.'''

        matches = xpath.find(self.pattern, self.doc)
        links = [m.getAttribute('sf:href') for m in matches]
        return [l.replace(self.strip, '') for l in links]
