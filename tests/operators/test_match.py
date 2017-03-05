import re
import pytest


def test_expect_match(should):
    'Hello foo bar' | should.match(r'Hello \w+ bar')
    'Hello foo BAR' | should.match.regexp(r'Hello \w+ bar', re.I)
    'Hello foo BAR' | should.match.regexp('BAR', re.I)

    with pytest.raises(AssertionError):
        should('foo bar').match('baz')

    with pytest.raises(AssertionError):
        'foo bar' | should.match.value('baz')

    with pytest.raises(AssertionError):
        'Hello foo BAR' | should.match.regexp(r'Hello \w+ bar')
