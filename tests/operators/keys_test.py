import pytest
from array import array


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

    {'foo': 'bar', 'fuu': 'bor'} | should.not_have.key('foobar')

    with pytest.raises(AssertionError):
        {'foo': 'bar', 'fuu': 'bor'} | should.not_have.key('foo')


def test_expect_keys(should):
    myDict = {'foo': 'bar', 'fuu': 'bor'}

    myDict | should.have.keys('foo', 'fuu')

    myDict | should.have.keys(('foo', 'fuu'))

    myDict | should.have.keys(['foo', 'fuu'])

    myDict | should.have.keys({'foo', 'fuu'})

    {1: 'bar', 2: 'bor'} | should.have.keys(array('i', [1, 2]))

    with pytest.raises(AssertionError):
        myDict | should.not_have.keys('foo', 'fuu')

    with pytest.raises(AssertionError):
        myDict | should.not_have.keys(('foo', 'fuu'))

    with pytest.raises(AssertionError):
        myDict | should.not_have.keys(['foo', 'fuu'])

    with pytest.raises(AssertionError):
        myDict | should.not_have.keys({'foo', 'fuu'})

    with pytest.raises(AssertionError):
        {1: 'bar', 2: 'bor'} | should.not_have.keys(array('i', [1, 2]))


def test_not_expect_keys(should):
    myDict = {'foo': 'baz', 'fuu': 'boz'}

    myDict | should.not_have.keys('foo', 'bar')

    myDict | should.not_have.keys(('foo', 'bar'))

    myDict | should.not_have.keys(['foo', 'bar'])

    myDict | should.not_have.keys({'foo', 'bar'})

    {1: 'baz', 2: 'boz'} | should.not_have.keys(array('i', [1, 5]))

    with pytest.raises(AssertionError):
        myDict | should.have.keys('foo', 'bar')

    with pytest.raises(AssertionError):
        myDict | should.have.keys(('foo', 'bar'))

    with pytest.raises(AssertionError):
        myDict | should.have.keys(['foo', 'bar'])

    with pytest.raises(AssertionError):
        myDict | should.have.keys({'foo', 'bar'})

    with pytest.raises(AssertionError):
        {1: 'baz', 2: 'boz'} | should.have.keys(array('i', [1, 5]))
