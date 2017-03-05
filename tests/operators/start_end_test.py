import pytest
from collections import OrderedDict


def test_start_end_with(should):
    # Strings
    'foo' | should.end_with.letter('o')
    'bar' | should.start_with.character('b')

    # Iterables
    [1, 2, 3] | should.start_with.number(1)
    [1, 2, 3] | should.end_with.number(2, 3)
    iter([1, 2, 3]) | should.start_with.numbers(1, 2)

    # Mappings
    OrderedDict([('foo', 0), ('bar', 1)]) | should.start_with('foo', 'bar')

    with pytest.raises(AssertionError):
        [1, 2, 3] | should.start_with.numbers(2, 3)

    with pytest.raises(AssertionError):
        'foo' | should.start_with.letter('o')
