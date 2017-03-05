import pytest
from grappa.operators.callable import CallableOperator


def test_should_callable(should):
    test_should_callable | should.be.callable
    (lambda x: x) | should.be.callable
    CallableOperator | should.be.callable
    CallableOperator.match | should.be.callable

    with pytest.raises(AssertionError):
        tuple() | should.be.callable

    with pytest.raises(AssertionError):
        0 | should.be.callable


def test_expect_callable(expect):
    test_expect_callable | expect.to.be.callable
    (lambda x: x) | expect.to.be.callable
    CallableOperator | expect.to.be.callable
    CallableOperator.match | expect.to.be.callable

    with pytest.raises(AssertionError):
        tuple() | expect.to.be.callable

    with pytest.raises(AssertionError):
        0 | expect.to.be.callable


def test_callable_operator(ctx):
    assert CallableOperator(ctx).match(lambda x: x) == (True, [])
    assert CallableOperator(ctx).match(CallableOperator) == (True, [])
    assert CallableOperator(ctx).match(CallableOperator.match) == (True, [])

    assert CallableOperator(ctx).match(0) == (False, [])
    assert CallableOperator(ctx).match('foo') == (False, [])
    assert CallableOperator(ctx).match(iter([1, 2, 3])) == (False, [])
    assert CallableOperator(ctx).match(None) == (
        False, ['a callable value cannot be "None"'])


def test_callable_operator_properties(should):
    (CallableOperator
        | should.have.property('kind')
        > should.be.equal.to('accessor'))

    (CallableOperator
        | should.have.property('operators')
        > should.have.length.of(1)
        > should.be.equal.to(('callable',)))

    CallableOperator | should.have.property('aliases') > should.be.empty

    CallableOperator | should.have.property('expected_message')
    CallableOperator | should.have.property('subject_message')

    (CallableOperator | should.have.property('information')
        > should.be.a('tuple')
        > should.have.length.of(2))
