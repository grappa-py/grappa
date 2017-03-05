import pytest


def test_should_type(should):
    'foo' | should.be.a(str)
    4 | should.be.an(int)
    {} | should.be.an(dict)
    tuple() | should.be.an(tuple)
    tuple() | should.be.instance.of('tuple')
    (lambda: True) | should.be.instance.of('lambda')

    def foo(): yield 1
    foo() | should.be.a('generator')

    class bar(object):
        def baz(self):
            pass

    bar | should.be.a('class')
    bar().baz | should.be.a('method')

    with pytest.raises(AssertionError):
        'foo' | should.be.an(int)

    with pytest.raises(AssertionError):
        [1, 2, 3] | should.be.a('tuple')
