from array import array
import pytest


def test_should_contain(should):
    'hello world' | should.contain('world') | should.contain('hello')
    'hello world' | should.contain('w') | should.contain('o')

    [1, 2, 3] | should.contain(1) | should.contain(3)

    ('foo', 'bar', 123) | should.contain('bar') | should.contain(123)

    {'foo', 'bar', 123} | should.contain('bar') | should.contain(123)

    [{'foo': 1}] | should.contain({'foo': 1})

    array('i', [1, 2, 3]) | should.contain(1) | should.contain(2)

    {'foo': 'bar', 'fuu': 2} | should.contain('bar') | should.contain(2)

    with pytest.raises(AssertionError):
        'hello world' | should.contain('planet')

    with pytest.raises(AssertionError):
        'hello world' | should.contain('t')

    with pytest.raises(AssertionError):
        [1, 2, 3] | should.contain(4)

    with pytest.raises(AssertionError):
        ('foo', 'bar', 123) | should.contain('baz')

    with pytest.raises(AssertionError):
        {'foo', 'bar', 123} | should.contain('baz')

    with pytest.raises(AssertionError):
        [{'foo': 1}] | should.contain({'foo': 2})

    with pytest.raises(AssertionError):
        array('i', [1, 2, 3]) | should.contain(4)

    with pytest.raises(AssertionError):
        {'foo': 'bar', 'fuu': 2} | should.contain('baz')


def test_should_contain_any(should):
    'hello world' | should.contain('world', 'hello')
    'hello world' | should.contain(('world', 'hello'))
    'hello world' | should.contain(['world', 'hello'])
    'hello world' | should.contain({'world', 'hello'})

    'hello world' | should.contain('w', 'o')
    'hello world' | should.contain(('w', 'o'))
    'hello world' | should.contain(['w', 'o'])
    'hello world' | should.contain({'w', 'o'})

    [1, 2, 3] | should.contain(1, 3)
    [1, 2, 3] | should.contain((1, 3))
    [1, 2, 3] | should.contain([1, 3])
    [1, 2, 3] | should.contain({1, 3})

    ('foo', 'bar', 123) | should.contain('bar', 123)
    {'foo', 'bar', 123} | should.contain(('bar', 123))
    {'foo', 'bar', 123} | should.contain({'bar', 123})
    {'foo', 'bar', 123} | should.contain(['bar', 123])

    [{'foo': 1}, {'bar': 2}] | should.contain({'foo': 1}, {'bar': 2})
    [{'foo': 1}, {'bar': 2}] | should.contain(({'foo': 1}, {'bar': 2}))
    [{'foo': 1}, {'bar': 2}] | should.contain([{'foo': 1}, {'bar': 2}])

    array('i', [1, 2, 3]) | should.contain(1, 2)
    array('i', [1, 2, 3]) | should.contain((1, 2))
    array('i', [1, 2, 3]) | should.contain({1, 2})
    array('i', [1, 2, 3]) | should.contain([1, 2])

    {'foo': 'bar', 'fuu': 'bor'} | should.contain('bar', 'bor')
    {'foo': 'bar', 'fuu': 'bor'} | should.contain(('bar', 'bor'))
    {'foo': 'bar', 'fuu': 'bor'} | should.contain(['bar', 'bor'])
    {'foo': 'bar', 'fuu': 'bor'} | should.contain({'bar', 'bor'})


def test_should_not_contain_any(should):
    'hello planet' | should._not.contain('world', 'hello')
    'hello planet' | should._not.contain(('world', 'hello'))
    'hello planet' | should._not.contain(['world', 'hello'])
    'hello planet' | should._not.contain({'world', 'hello'})

    'hello planet' | should._not.contain('w', 'o')
    'hello planet' | should._not.contain(('w', 'o'))
    'hello planet' | should._not.contain(['w', 'o'])
    'hello planet' | should._not.contain({'w', 'o'})

    [1, 2, 3] | should._not.contain(1, 4)
    [1, 2, 3] | should._not.contain((1, 4))
    [1, 2, 3] | should._not.contain([1, 4])
    [1, 2, 3] | should._not.contain({1, 4})

    ('foo', 'bar', 123) | should._not.contain('baz', 123)
    {'foo', 'bar', 123} | should._not.contain(('baz', 123))
    {'foo', 'bar', 123} | should._not.contain({'baz', 123})
    {'foo', 'bar', 123} | should._not.contain(['baz', 123])

    [{'foo': 1}, {'bar': 2}] | should._not.contain({'foo': 1}, {'baz': 2})
    [{'foo': 1}, {'bar': 2}] | should._not.contain(({'foo': 1}, {'baz': 2}))
    [{'foo': 1}, {'bar': 2}] | should._not.contain([{'foo': 1}, {'baz': 2}])

    array('i', [1, 2, 3]) | should._not.contain(1, 4)
    array('i', [1, 2, 3]) | should._not.contain((1, 4))
    array('i', [1, 2, 3]) | should._not.contain({1, 4})
    array('i', [1, 2, 3]) | should._not.contain([1, 4])

    {'foo': 'bar', 'fuu': 'bor'} | should._not.contain('baz', 'bor')
    {'foo': 'bar', 'fuu': 'bor'} | should._not.contain(('baz', 'bor'))
    {'foo': 'bar', 'fuu': 'bor'} | should._not.contain(['baz', 'bor'])
    {'foo': 'bar', 'fuu': 'bor'} | should._not.contain({'baz', 'bor'})


def test_should_contain_failures(should):
    with pytest.raises(AssertionError):
        () | should.contain('bar')

    with pytest.raises(AssertionError):
        1 | should.contain('bar')
