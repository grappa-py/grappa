import pytest


def test_pass_function(should):
    def test(subject):
        return len(subject) == 3, []

    'foo' | should.pass_test(test)
    'fo' | should.do_not.pass_test(test)

    with pytest.raises(AssertionError):
        'foo' | should.do_not.pass_test(test)
