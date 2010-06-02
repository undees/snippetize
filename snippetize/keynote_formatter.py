from pygments.formatter import Formatter
from pygments.token import Token
from cgi import escape

class KeynoteFormatter(Formatter):
    '''Pygments formatter that outputs XML for Keynote slides.'''

    def __init__(self, styles):
        '''Takes a dictionary from style names to numbers
        (these numbers are assigned by Keynote).  Example:
            {
                'Keyword':41,
                'Name.Class':40,
                'Name.Function':47,
                'Literal':46,
                'Paragraph':387,
                'Commment':45,
                'Operator':41,
            }'''

        Formatter.__init__(self)

        def style_name(item):
            name, style = item
            if name == 'Paragraph':
                style = 'SFWPParagraphStyle-%s' % str(style)
            else:
                style = 'SFWPCharacterStyle-%s' % str(style)
            return (name, style)

        self.styles = dict(map(style_name, styles.items()))

    def style_for_ttype(self, ttype):
        '''Called by format() to find the right character /
        paragraph style for the given type of text.'''

        parts = str(ttype).split('.')
        name = '.'.join(parts[1:])
        gen_name = parts[1]

        if name in self.styles:
            return self.styles[name]
        elif gen_name in self.styles:
            return self.styles[gen_name]
        else:
            return None

    def format(self, tokensource, outfile):
        '''Called by Pygments when it's time to write a chunk
        of code to an output stream.'''

        outfile.write('<sf:p sf:style="%s" sf:list-level="1">'
                      % self.styles['Paragraph'])

        for ttype, value in tokensource:
            style = self.style_for_ttype(ttype)
            text = escape(value).replace('\n', '<sf:lnbr/>')

            if style:
                outfile.write('<sf:span sf:style="%s">%s</sf:span>'
                              % (style, text))
            else:
                outfile.write(text)

        outfile.write('</sf:p>')
