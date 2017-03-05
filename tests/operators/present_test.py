import pytest


def test_should_present(should):
    1 | should.be.present
    'foo' | should.be.present
    [1, 2, 3] | should.be.present
    (1, 2, 3) | should.be.present
    iter([1]) | should.be.present
    {'foo': True} | should.be.present

    '' | should.not_be.present
    0 | should.not_be.present
    None | should.not_be.present
    [] | should.not_be.present
    tuple() | should.not_be.present
    dict() | should.not_be.present

    with pytest.raises(AssertionError):
        'foo' | should.do_not.exists

    with pytest.raises(AssertionError):
        None | should.be.present

    with pytest.raises(AssertionError):
        None | should.exists

    with pytest.raises(AssertionError):
        0 | should.exists

    with pytest.raises(AssertionError):
        [] | should.exists

    with pytest.raises(AssertionError):
        tuple() | should.exists
