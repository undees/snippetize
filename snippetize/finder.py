import xpath

class Finder:
    def __init__(self, doc, pattern, strip):
        self.doc     = doc
        self.pattern = pattern
        self.strip   = strip

    def snippets(self):
        matches = xpath.find(self.pattern, self.doc)
        links = [m.getAttribute('sf:href') for m in matches]
        return [l.replace(self.strip, '') for l in links]
