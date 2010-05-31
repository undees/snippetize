from itertools import dropwhile, takewhile
import re

class Extractor:
    def __init__(self, parts):
        self.parts = parts

    def extract(self, code, part = ''):
        if len(part) == 0:
            return code

        start, end = self.parts[part]
        onepast = OnePast()

        all_lines = code.split('\n')
        no_header = dropwhile(lambda s: start not in s, all_lines)
        no_footer = takewhile(lambda s: onepast(end not in s), no_header)
        snipped_lines = list(no_footer)

        return '\n'.join(unindent(snipped_lines))

def spaces(str):
    return re.match(' *', str).end()

def unindent(lines):
    amount = reduce(lambda s, t: min(spaces(s), spaces(t)), lines)
    return [line[amount:] for line in lines]

class OnePast:
    def __init__(self):
        self.triggered = False
        self.called = False

    def __call__(self, condition):
        self.called = self.triggered
        self.triggered = self.triggered or (not condition)
        return (not self.called) or (not self.triggered)
