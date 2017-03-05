import pytest


def test_should_within(should):
    10 | should.be.between(5, 10)
    101 | should.be.within(100, 102)

    # negation
    11 | should.not_be.between(5, 9)

    with pytest.raises(AssertionError):
        10 | should.not_be.between.to(5, 10)

    with pytest.raises(AssertionError):
        None | should.be.between.numbers(10, 10)
