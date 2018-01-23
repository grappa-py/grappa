import pytest
from functools import partial


def test_raises(should):
    def error():
        raise AssertionError('foo')

    def error_with_params(foo_param):
        raise AssertionError(foo_param)

    error | should.raise_error(AssertionError)
    error | should.do_not.raise_error(NotImplementedError)

    partial(error_with_params, "Foobar") | should.raise_error(AssertionError)
    partial(error_with_params, "Foobar") | should.to_not\
        .raise_error(NotImplementedError)

    with pytest.raises(AssertionError):
        error | should.raise_error(NotImplementedError)

    with pytest.raises(AssertionError):
        error | should.do_not.raise_error(AssertionError)

    with pytest.raises(AssertionError):
        None | should.raise_error(AssertionError)
