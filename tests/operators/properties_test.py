import pytest


def test_expect_properties(should):
    class foo(object):
        foo = 'bar'

        def bar(self):
            pass

    foo() | should.have.property('foo')
    foo() | should.have.property('foo') > should.be.equal.to('bar')

    should(foo()).have.property('foo') > should.be.equal.to('bar')
    should(foo()).have.property('foo').which.should.be.equal.to('bar')

    should(foo()).have.property('bar').which.should.be.a('method')

    should(foo()).have.properties('bar', 'foo')

    with pytest.raises(AssertionError):
        should(foo()).have.property('baz')

    with pytest.raises(AssertionError):
        should(foo()).have.property('baz')

    with pytest.raises(AssertionError):
        should(foo()).have.property('foo') > should.be.equal.to('foo')

    with pytest.raises(AssertionError):
        should(foo()).have.property('foo').which.should.be.equal.to('pepe')
