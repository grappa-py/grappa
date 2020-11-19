import pytest


def test_implements(should):
    class foo(object):
        foo = None

        def bar(self):
            pass

        def baz(self):
            pass

    foo | should.implements.methods('bar', 'baz')
    foo | should.do_not.implements.methods('foo')

    with pytest.raises(AssertionError):
        foo | should.implement.methods('foo', 'faa')

    with pytest.raises(AssertionError):
        foo | should.implements.methods(2, False)
