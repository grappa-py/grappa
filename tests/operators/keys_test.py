import pytest


def test_expect_keys(should):
    {'foo': 'bar'} | should.have.key('foo')
    {'foo': 'bar'} | should.have.key('foo') > should.be.equal.to('bar')
    'bar' | should.be.equal.to('bar')

    ({'foo': {'bar': True}}
        | should.have.key('foo')
        > should.be.a('dict')
        > should.have.length.of(1)
        > should.have.key('bar')
        > should.be.true)

    should({'foo': 'bar'}).have.key('foo') > should.be.equal.to('bar')
    should({'foo': 'bar'}).have.key('foo').which.should.be.equal.to('bar')

    with pytest.raises(AssertionError):
        {'foo': 'bar'} | should.have.key('bar')

    with pytest.raises(AssertionError):
        [] | should.have.key('bar')

    with pytest.raises(AssertionError):
        should({'foo': 'bar'}).have.key('foo') > should.be.equal.to('foo')

    with pytest.raises(AssertionError):
        should({'foo': 'bar'}).have.key('foo').which.should.be.equal.to('pepe')


def test_not_expected_keys(should):
    {'foo': 'bar'} | should.not_have.key('foobar')

    {'foo': 'bar', 'fuu': True} | should.not_have.key('foobar')

    {'foo': 'bar', 'fuu': True} | should.not_have.keys('foobar', 'fuubar')

    with pytest.raises(AssertionError):
        {'foo': 'bar', 'fuu': True} | should.not_have.key('foo')

    with pytest.raises(AssertionError):
        {'foo': 'bar', 'fuu': True} | should.not_have.keys('foo', 'fuu')