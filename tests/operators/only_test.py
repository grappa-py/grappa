# coding: utf-8
import pytest
try:
    from unittest import mock
except ImportError:
    import mock


def test_should_contain_only(should):
    [1, 2] | should.contain.only(1, 2)
    # dicts/list + different order in expected values
    [{'foo': 'bar'}, 2] | should.contain.only(2, {'foo': 'bar'})
    ('foo', 'bar', 123) | should.contain.only('bar', 123, 'foo')
    'hello' | should.contain.only('hello')  # string case
    # chainability
    ([], 'ab', 42) | should.contain.only(42, 'ab', []) | should.have.length(3)

    with pytest.raises(AssertionError):
        ['a', '∆˚'] | should.contain.only('a')  # missing items

    with pytest.raises(AssertionError):
        'abc' | should.contain.only('def')  # string case unequal

    with pytest.raises(AssertionError):
        [321, '∆˚'] | should.contain.only('∆˚', 'b')  # different item

    with pytest.raises(AssertionError):
        # too many items
        [
            {'foo': 'bar'},
            {'meaning': 42}
        ] | should.contain.only([], {'foo': 'bar'}, {'meaning': 42})


def test_should_contain_only_string_case(should):
    """Should log a warning when using the only operator for strings."""
    with mock.patch('grappa.operators.only.log') as log:
        'lala' | should.contain.only('lala')
        log.warn.assert_called_once_with(
            'String comparison using "only" is not advised'
        )
