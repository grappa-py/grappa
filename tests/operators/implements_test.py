import pytest


def test_implements(should):
    class foo(object):
        foo = None

        def bar():
            pass

        def baz():
            pass

    foo | should.implements.methods('bar', 'baz')
    foo | should.do_not.implements.methods('foo')

    with pytest.raises(AssertionError):
        foo | should.implement.methods('foo', 'faa')
