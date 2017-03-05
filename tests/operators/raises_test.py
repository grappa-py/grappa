import pytest


def test_raises(should):
    def error():
        raise AssertionError('foo')

    error | should.raise_error(AssertionError)
    error | should.do_not.raise_error(NotImplementedError)

    with pytest.raises(AssertionError):
        error | should.raise_error(NotImplementedError)

    with pytest.raises(AssertionError):
        error | should.do_not.raise_error(AssertionError)

    with pytest.raises(AssertionError):
        None | should.raise_error(AssertionError)
