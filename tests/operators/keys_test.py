import pytest


def test_expect_key(should):
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


def test_not_expect_key(should):
    {'foo': 'bar'} | should.not_have.key('foobar')

    {'foo': 'bar', 'fuu': True} | should.not_have.key('foobar')

    with pytest.raises(AssertionError):
        {'foo': 'bar', 'fuu': True} | should.not_have.key('foo')


def test_expect_keys(should):
    myDict = {'foo': 'bar', 'fuu': 'bor', 'fii': True}

    myDict | should.have.keys('foo', 'fii')

    myDict | should.have.keys(('foo', 'fii'))

    myDict | should.have.keys(['foo', 'fii'])

    myDict | should.have.keys({'foo', 'fii'})

    with pytest.raises(AssertionError):
        myDict | should.not_have.keys('foo', 'fii')

    with pytest.raises(AssertionError):
        myDict | should.not_have.keys(('foo', 'fii'))

    with pytest.raises(AssertionError):
        myDict | should.not_have.keys(['foo', 'fii'])

    with pytest.raises(AssertionError):
        myDict | should.not_have.keys({'foo', 'fii'})


def test_not_expect_keys(should):
    myDict = {'foo': 'bar', 'fuu': 'bor', 'fii': True}

    myDict | should.not_have.keys('bar', 'bor')

    myDict | should.not_have.keys(('bar', 'bor'))

    myDict | should.not_have.keys(['bar', 'bor'])

    myDict | should.not_have.keys({'bar', 'bor'})

    with pytest.raises(AssertionError):
        myDict | should.have.keys('bar', 'bor')

    with pytest.raises(AssertionError):
        myDict | should.have.keys(('bar', 'bor'))

    with pytest.raises(AssertionError):
        myDict | should.have.keys(['bar', 'bor'])

    with pytest.raises(AssertionError):
        myDict | should.have.keys({'bar', 'bor'})
