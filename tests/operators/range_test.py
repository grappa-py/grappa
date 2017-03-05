import pytest


def test_expect_below(should):
    10 | should.be.below(100)
    1 | should.be.below.of(2)
    10 | should.be.lower.than(100)

    # negation
    10 | should.not_be.below.of(2)
    10 | should.not_be.lower.than(2)

    with pytest.raises(AssertionError):
        10 | should.be.below.of(2)

    with pytest.raises(AssertionError):
        None | should.be.below.of(10)


def test_expect_above(should):
    10 | should.be.above(9)
    3 | should.be.above.of(2)

    # negation
    10 | should.not_be.above.of(11)

    with pytest.raises(AssertionError):
        10 | should.be.above.of(100)

    with pytest.raises(AssertionError):
        None | should.be.above.of(10)


def test_expect_below_or_equal(should):
    10 | should.be.below_or_equal(10)
    5 | should.be.below_or_equal(10)

    # negation
    10 | should.not_be.below_or_equal.to(5)

    with pytest.raises(AssertionError):
        10 | should.not_be.below_or_equal.to(10)

    with pytest.raises(AssertionError):
        None | should.be.below_or_equal.of(10)


def test_expect_above_or_equal(should):
    10 | should.be.above_or_equal(10)
    101 | should.be.above_or_equal(100)
    3 | should.be.above_or_equal.to(3)

    # negation
    10 | should.not_be.above_or_equal.to(100)

    with pytest.raises(AssertionError):
        10 | should.not_be.above_or_equal.to(10)

    with pytest.raises(AssertionError):
        None | should.be.above_or_equal.of(10)
