import pytest


def test_expect_length(should):
    [] | should.have.length.of(0)
    'foo' | should.have.length.of(3) | should.have.length(3)
    'foo' | should.not_have.length.of(4)
    'foo' | should.not_have.length.of(0) | should.not_have.length.of(2)

    with pytest.raises(AssertionError):
        'foo' | should.have.length(0)

    with pytest.raises(AssertionError):
        'foo' | should.have.length.of(3) | should.have.length(5)

    with pytest.raises(AssertionError):
        None | should.have.length(0)

    with pytest.raises(AssertionError):
        'foo' | should.not_have.length.of(3)
