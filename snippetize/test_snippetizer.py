from snippetize.snippetizer import Snippetizer
import filecmp

def test_snippetizer():
    snippetizer = Snippetizer('all.key', 'out.key', 'config.py')
    snippetizer.snippetize()
    assert(filecmp.cmp('out.key', 'new.key'))
