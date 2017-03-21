import pytest
from grappa.operators.none import NoneOperator


def test_should_none(should):
    None | should.be.none
    'foo' | should.not_be.none

    with pytest.raises(RuntimeError):
        'foo' | should.not_be.none.to.be.equal(None)

    with pytest.raises(AssertionError):
        False | should.be.none

    with pytest.raises(AssertionError):
        None | should.not_be.none

    with pytest.raises(AssertionError):
        'foo' | should.be.none

    with pytest.raises(AssertionError):
        [1, 2, 3] | should.be.none


def test_expect_none(expect):
    None | expect.to.be.none

    with pytest.raises(AssertionError):
        False | expect.to.be.none

    with pytest.raises(AssertionError):
        'foo' | expect.to.be.none

    with pytest.raises(AssertionError):
        [1, 2, 3] | expect.to.be.none


def test_none_operator(ctx):
    assert NoneOperator(ctx).match(None) == (True, [])
    assert NoneOperator(ctx).match(1) == (False, [])
