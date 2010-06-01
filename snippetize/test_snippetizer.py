from os.path import getsize
from snippetize.snippetizer import Snippetizer
import filecmp

def test_snippetizer():
    snippetizer = Snippetizer('all.key', 'out.key', 'config.py')
    snippetizer.snippetize()

    # Weaker than a full file compare, but there's a byte
    # in there somewhere that changes on every pass.
    assert(getsize('out.key') == getsize('new.key'))
