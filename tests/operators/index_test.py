# import pytest


def test_index(should):
    [1, 2, 3] | should.have.index(2)
    (1, 2, 3) | should.have.index(1)
    (1, 2, 3) | should.have.index(2).to.be.equal(3)

    [1] | should.have.length.of(1).to.have.index.at(0)

    # ({'foo': {'bar': True}}
    #     | should.have.key('foo')
    #     > should.be.a('dict')
    #     > should.have.key('bar')
    #     > should.be.equal.to({'bar': True}))
    #
    # should({'foo': 'bar'}).have.key('foo') > should.be.equal.to('bar')
    # should({'foo': 'bar'}).have.key('foo').which.should.be.equal.to('bar')
    #
    # with pytest.raises(AssertionError):
    #     {'foo': 'bar'} | should.have.key('bar')
    #
    # with pytest.raises(AssertionError):
    #     [] | should.have.key('bar')
    #
    # with pytest.raises(AssertionError):
    #     should({'foo': 'bar'}).have.key('foo') > should.be.equal.to('foo')
    #
    # with pytest.raises(AssertionError):
    #     (should({'foo': 'bar'}).have.key('foo')
    #         .which.should.be.equal.to('pepe'))
