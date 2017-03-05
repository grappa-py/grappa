import pytest
from grappa.operators.empty import EmptyOperator


def test_should_empty(should):
    None | should.be.empty
    [] | should.be.empty
    '' | should.be.empty
    tuple() | should.be.empty
    0 | should.be.empty
    iter([]) | should.be.empty

    with pytest.raises(AssertionError):
        False | should.be.empty

    with pytest.raises(AssertionError):
        True | should.be.empty

    with pytest.raises(AssertionError):
        'foo' | should.be.empty

    with pytest.raises(AssertionError):
        [1, 2, 3] | should.be.empty

    with pytest.raises(AssertionError):
        iter([1, 2, 3]) | should.be.empty


def test_expect_empty(expect):
    None | expect.to.be.empty
    [] | expect.to.be.empty
    '' | expect.to.be.empty
    tuple() | expect.to.be.empty
    0 | expect.to.be.empty
    iter([]) | expect.to.be.empty

    with pytest.raises(AssertionError):
        False | expect.to.be.empty

    with pytest.raises(AssertionError):
        True | expect.to.be.empty

    with pytest.raises(AssertionError):
        'foo' | expect.to.be.empty

    with pytest.raises(AssertionError):
        [1, 2, 3] | expect.to.be.empty

    with pytest.raises(AssertionError):
        iter([1, 2, 3]) | expect.to.be.empty


def test_empty_operator(ctx):
    assert EmptyOperator(ctx).match(0) is True
    assert EmptyOperator(ctx).match(None) is True
    assert EmptyOperator(ctx).match('') is True
    assert EmptyOperator(ctx).match(iter([])) is True

    assert EmptyOperator(ctx).match(True) is False
    assert EmptyOperator(ctx).match(False) is False
    assert EmptyOperator(ctx).match('foo') is False
    assert EmptyOperator(ctx).match(123) is False
    assert EmptyOperator(ctx).match(0.2321) is False
    assert EmptyOperator(ctx).match(iter([1, 2, 3])) is False


def test_empty_operator_properties(should):
    (EmptyOperator
        | should.have.property('kind')
        > should.be.equal.to('accessor'))

    (EmptyOperator
        | should.have.property('operators')
        > should.have.length.of(1)
        > should.be.equal.to(('empty',)))

    EmptyOperator | should.have.property('aliases') > should.be.empty

    EmptyOperator | should.have.property('expected_message')
    EmptyOperator | should.have.property('subject_message')

    (EmptyOperator | should.have.property('information')
        > should.be.a('tuple')
        > should.have.length.of(1))
