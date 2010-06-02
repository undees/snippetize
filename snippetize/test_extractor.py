from snippetize.extractor import Extractor

def test_extractor():
    code = '''
class Foo:
  def bar:
    pass

  def baz:
    pass
'''

    parts = {'bar': ['def bar', 'pass']}

    extractor = Extractor(parts)

    assert(extractor.extract(code) == code)
    assert(extractor.extract(code, 'bar') == 'def bar:\n  pass')
