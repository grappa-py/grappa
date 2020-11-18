from array import array
import pytest


def test_should_contain(should):
    'hello world' | should.contain('world') | should.contain('hello')
    'hello world' | should.contain('w') | should.contain('o')

    [1, 2, 3] | should.contain(1) | should.contain(3)

    ('foo', 'bar', 123) | should.contain('bar') | should.contain(123)

    {'foo', 'bar', 123} | should.contain('bar') | should.contain(123)

    array('i', [1, 2]) | should.contain(1) | should.contain(2)

    [{'foo': 1}] | should.contain({'foo': 1})

    {'foo': 'bar', 'fuu': 2} | should.contain('bar') | should.contain(2)

    with pytest.raises(AssertionError):
        'hello world' | should.contain('planet')

    with pytest.raises(AssertionError):
        [1, 2, 3] | should.contain(4)


def test_should_contain_all(should):
    'hello world' | should.contain('world', 'hello')
    'hello world' | should.contain('w', 'o')

    [1, 2, 3] | should.contain(1, 3)

    ('foo', 'bar', 123) | should.contain('bar', 123)

    {'foo', 'bar', 123} | should.contain('bar', 123)

    array('i', [1, 2]) | should.contain(1, 2)

    [{'foo': 1}, {'bar': 2}] | should.contain({'foo': 1}, {'bar': 2})

    {'foo': 'bar', 'fuu': 'bor'} | should.contain('bar', 'bor')


def test_should_contain_failures(should):
    with pytest.raises(AssertionError):
        () | should.contain('bar')

    with pytest.raises(AssertionError):
        1 | should.contain('bar')
