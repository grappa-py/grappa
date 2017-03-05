import pytest
import grappa
from grappa import api


def test_api(should):
    for symbol in api.__all__:
        grappa | should.have.property(symbol)


def test_should_api_constructor(should):
    should('foo').to.be.equal('foo')

    with pytest.raises(AssertionError):
        should('foo').to.be.equal('bar')


def test_expect_api_constructor(expect):
    expect('foo').to.be.equal('foo')

    with pytest.raises(AssertionError):
        expect('foo').to.be.equal('bar')
