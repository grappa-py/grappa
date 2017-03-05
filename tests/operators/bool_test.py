import pytest
from grappa.operators.bool import TrueOperator, FalseOperator


def test_should_true(should):
    True | should.be.true

    with pytest.raises(AssertionError):
        False | should.be.true

    with pytest.raises(AssertionError):
        None | should.be.true

    with pytest.raises(AssertionError):
        'foo' | should.be.true

    with pytest.raises(AssertionError):
        [1, 2, 3] | should.be.true


def test_expect_true(expect):
    True | expect.to.be.true

    with pytest.raises(AssertionError):
        False | expect.to.be.true

    with pytest.raises(AssertionError):
        None | expect.to.be.true

    with pytest.raises(AssertionError):
        'foo' | expect.to.be.true

    with pytest.raises(AssertionError):
        [1, 2, 3] | expect.to.be.true


def test_should_false(should):
    False | should.be.false

    with pytest.raises(AssertionError):
        True | should.be.false

    with pytest.raises(AssertionError):
        None | should.be.false

    with pytest.raises(AssertionError):
        'foo' | should.be.false

    with pytest.raises(AssertionError):
        [1, 2, 3] | should.be.false


def test_expect_false(expect):
    False | expect.to.be.false

    with pytest.raises(AssertionError):
        True | expect.to.be.false

    with pytest.raises(AssertionError):
        None | expect.to.be.false

    with pytest.raises(AssertionError):
        'foo' | expect.to.be.false

    with pytest.raises(AssertionError):
        [1, 2, 3] | expect.to.be.false


def test_true_operator(ctx):
    assert TrueOperator(ctx).match(True) == (True, [])
    assert TrueOperator(ctx).match(False) == (False, [])

    assert TrueOperator(ctx).match(0) == (False,
                                          ['subject is not a bool type'])


def test_true_operator_message(should):
    (TrueOperator
        | should.have.property('kind')
        > should.be.equal.to('accessor'))

    (TrueOperator
        | should.have.property('operators')
        > should.be.equal.to(('true',)))

    TrueOperator | should.have.property('aliases') > should.be.empty

    TrueOperator | should.have.property('expected_message')


def test_false_operator(ctx):
    assert FalseOperator(ctx).match(False) == (True, [])
    assert FalseOperator(ctx).match(True) == (False, [])

    assert FalseOperator(ctx).match(0) == (False,
                                           ['subject is not a bool type'])


def test_false_operator_message(should):
    (FalseOperator
        | should.have.property('kind')
        > should.be.equal.to('accessor'))

    (FalseOperator
        | should.have.property('operators')
        > should.be.equal.to(('false',)))

    FalseOperator | should.have.property('aliases') > should.be.empty

    FalseOperator | should.have.property('expected_message')
