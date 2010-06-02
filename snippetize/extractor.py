from itertools import dropwhile, takewhile
from sys import maxint
import re

class Extractor:
    '''Extracts snippets from source code.'''

    def __init__(self, parts):
        '''Stores a dictionary of snippet specfications,
        of the form: {'name': ['start_line', 'end_line']}'''

        self.parts = parts

    def extract(self, code, part = ''):
        '''Returns the portion of a string of source code
        indicated by the given snippet name (or the whole
        string if the name is empty).'''

        if len(part) == 0:
            return code

        start, end = self.parts[part]
        onepast = _OnePast()

        all_lines = code.split('\n')
        no_header = dropwhile(lambda s: start not in s, all_lines)
        no_footer = takewhile(lambda s: onepast(end not in s), no_header)
        snipped_lines = list(no_footer)

        return '\n'.join(_unindent(snipped_lines))

def _leading_spaces(str):
    '''Returns the number of leading spaces in a string.
    does not account for tabs.'''

    return re.match(' *', str).end()

def _unindent(lines):
    '''Removes the same number of leading spaces
    from each line in a list, until at least one
    line has no leading space.'''

    amount = reduce(lambda n, s: min(n, _leading_spaces(s)), lines, maxint)
    return [line[amount:] for line in lines]

class _OnePast:
    '''Callable class for use with itertools' takewhile().
    Helps the user of the collection take one past the
    target element.'''

    def __init__(self):
        '''A new object hasn't been called or triggered yet.'''

        self.triggered = False
        self.called = False

    def __call__(self, condition):
        '''Returns True until one call *after* the condition
        is True.'''

        self.called = self.triggered
        self.triggered = self.triggered or (not condition)
        return (not self.called) or (not self.triggered)
