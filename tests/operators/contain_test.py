import pytest


def test_should_contain(should):
    'hello world' | should.contain('world') | should.contain('hello')
    'hello world' | should.contain('w') | should.contain('o')

    [1, 2, 3] | should.contain(1) | should.contain(3)
    ('foo', 'bar', 123) | should.contain('bar') | should.contain(123)
    [{'foo': 1}] | should.contain({'foo': 1})

    with pytest.raises(AssertionError):
        'hello world' | should.contain('planet')

    with pytest.raises(AssertionError):
        [1, 2, 3] | should.contain(4)
