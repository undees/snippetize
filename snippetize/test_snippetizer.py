from snippetize.snippetizer import Snippetizer
import filecmp

def test_snippetizer():
    snippetizer = Snippetizer('all.key', 'config.py')
    snippetizer.snippetize()
    assert(filecmp.cmp('all.key', 'new.key'))
