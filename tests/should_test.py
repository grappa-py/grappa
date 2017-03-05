import re
import pytest
from grappa import expect, should, config

# Enable debug mode
config.debug = False


def test_bool():
    True | should.be.true | should.be.present
    False | should.be.false | should.be.equal.to(False)
    False | should.be.false | should.not_be.equal.to(True)

    with pytest.raises(AssertionError):
        True | should.be.false

    with pytest.raises(AssertionError):
        False | should.be.true

    should(True).be.true

    should('foo').be.present
    'pee' | should.be.equal('pee') | should.have.length.of(3)

    expect('foo').to.be.equal('foo')


def test_should_be_callable():
    (lambda: True) | should.be.callable

    with pytest.raises(AssertionError):
        'foo' | should.be.callable

    with pytest.raises(AssertionError):
        None | should.be.callable


# def test_should_be_true_false():
#     True | should.be.true
#     False | should.be.false
#
#     with pytest.raises(AssertionError):
#         False | should.be.true
#
#     with pytest.raises(AssertionError):
#         None | should.be.false


def test_expect_api():
    expect('foo').to.be.equal('foo')

    with pytest.raises(AssertionError):
        expect('foo').to.be.equal('bar')


def test_expect_empty():
    [] | should.be.empty
    tuple() | should.be.empty
    '' | should.be.empty
    0 | should.be.empty

    with pytest.raises(AssertionError):
        'foo' | should.be.empty

    with pytest.raises(AssertionError):
        iter('foo') | should.be.empty

    with pytest.raises(AssertionError):
        (1, 2, 3) | should.be.empty


def test_expect_none():
    [] | should.not_be.none
    None | should.be.none
    'foo' | should.not_be.none
    # None | should.not_be.none

    with pytest.raises(AssertionError):
        'foo' | should.be.none

    with pytest.raises(AssertionError):
        None | should.not_be.none


def test_expect_length():
    [] | should.have.length.of(0)
    'foo' | should.have.length.of(3) | should.have.length(3)
    'foo' | should.not_have.length.of(4)
    'foo' | should.not_have.length.of(0) | should.not_have.length.of(2)

    with pytest.raises(AssertionError):
        'foo' | should.have.length(0)

    with pytest.raises(AssertionError):
        'foo' | should.have.length.of(3) | should.have.length(5)

    with pytest.raises(AssertionError):
        None | should.have.length(0)

    with pytest.raises(AssertionError):
        'foo' | should.not_have.length.of(3)


def test_should_be_type():
    'foo' | should.be.a(str)
    4 | should.be.an(int)
    {} | should.be.an(dict)
    tuple() | should.be.an(tuple)
    tuple() | should.be.instance.of('tuple')
    (lambda: True) | should.be.instance.of('lambda')

    def foo(): yield 1
    foo() | should.be.a('generator')

    class bar(object):
        def baz(self):
            pass

    bar | should.be.a('class')
    bar().baz | should.be.a('method')


def test_expect_contain():
    'hello foo' | should.contain('foo')

    with pytest.raises(AssertionError):
        'hello foo' | should.contain('bar')

    with pytest.raises(AssertionError):
        'bar' | should.contain('foo')


def test_expect_keys():
    {'foo': 'bar'} | should.have.key('foo')
    {'foo': 'bar'} | should.have.key('foo') > should.be.equal.to('bar')
    'bar' | should.be.equal.to('bar')

    should({'foo': 'bar'}).have.key('foo') > should.be.equal.to('bar')
    should({'foo': 'bar'}).have.key('foo').which.should.be.equal.to('bar')

    with pytest.raises(AssertionError):
        {'foo': 'bar'} | should.have.key('bar')

    with pytest.raises(AssertionError):
        [] | should.have.key('bar')

    with pytest.raises(AssertionError):
        should({'foo': 'bar'}).have.key('foo') > should.be.equal.to('foo')

    with pytest.raises(AssertionError):
        should({'foo': 'bar'}).have.key('foo').which.should.be.equal.to('pepe')


def test_expect_properties():
    class foo(object):
        foo = 'bar'

    foo() | should.have.property('foo')
    foo() | should.have.property('foo') > should.be.equal.to('bar')

    should(foo()).have.property('foo') > should.be.equal.to('bar')
    should(foo()).have.property('foo').which.should.be.equal.to('bar')

    with pytest.raises(AssertionError):
        should(foo()).have.property('bar')

    with pytest.raises(AssertionError):
        should(foo()).have.property('bar')

    with pytest.raises(AssertionError):
        should(foo()).have.property('foo') > should.be.equal.to('foo')

    with pytest.raises(AssertionError):
        should(foo()).have.property('foo').which.should.be.equal.to('pepe')


def test_expect_match():
    'Hello foo bar' | should.match(r'Hello \w+ bar')
    'Hello foo BAR' | should.match.regexp(r'Hello \w+ bar', re.I)
    'Hello foo BAR' | should.match.regexp('BAR', re.I)

    with pytest.raises(AssertionError):
        should('foo bar').match('baz')

    with pytest.raises(AssertionError):
        'foo bar' | should.match.value('baz')

    with pytest.raises(AssertionError):
        'Hello foo BAR' | should.match.regexp(r'Hello \w+ bar')


def test_expect_below():
    10 | should.be.below(100)
    1 | should.be.below.of(2)
    10 | should.be.lower.than(100)

    # negation
    10 | should.not_be.below.of(2)
    10 | should.not_be.lower.than(2)

    with pytest.raises(AssertionError):
        10 | should.be.below.of(2)

    with pytest.raises(AssertionError):
        None | should.be.below.of(10)


def test_expect_above():
    10 | should.be.above(9)
    3 | should.be.above.of(2)

    # negation
    10 | should.not_be.above.of(11)

    with pytest.raises(AssertionError):
        10 | should.be.above.of(100)

    with pytest.raises(AssertionError):
        None | should.be.above.of(10)


def test_expect_below_or_equal():
    10 | should.be.below_or_equal(10)
    5 | should.be.below_or_equal(10)

    # negation
    10 | should.not_be.below_or_equal.to(5)

    with pytest.raises(AssertionError):
        10 | should.not_be.below_or_equal.to(10)

    with pytest.raises(AssertionError):
        None | should.be.below_or_equal.of(10)


def test_expect_above_or_equal():
    10 | should.be.above_or_equal(10)
    101 | should.be.above_or_equal(100)
    3 | should.be.above_or_equal.to(3)

    # negation
    10 | should.not_be.above_or_equal.to(100)

    with pytest.raises(AssertionError):
        10 | should.not_be.above_or_equal.to(10)

    with pytest.raises(AssertionError):
        None | should.be.above_or_equal.of(10)


def test_expect_between():
    10 | should.be.between(5, 10)
    101 | should.be.within(100, 102)

    # negation
    11 | should.not_be.between(5, 9)

    with pytest.raises(AssertionError):
        10 | should.not_be.between.to(5, 10)

    with pytest.raises(AssertionError):
        None | should.be.between.numbers(10, 10)


def test_expect_context_manager():
    should('foo').be.equal('foo')

    with should('foo'):
        should.be.equal('foo')
        should.have.length.of(3)
        should.have.type('string')

    with should('foo'):
        should.be.a('string').which.has.length.of(3)
        should.be.equal('foo')

    should('foo').be.equal('foo')
    'foo' | should.be.equal('foo')

    with pytest.raises(AssertionError):
        with should('foo'):
            should.be.equal('foo')
            should.have.length.of(5)


def test_all_composition():
    'foo' | should.all(should.be.a('string'), should.have.length.to(3))

    'foo' | should.any(should.be.a('number'), should.have.length.to(3))

    with pytest.raises(AssertionError):
        'foo' | should.all(should.be.a('string'), should.have.length.to(5))

    with pytest.raises(AssertionError):
        'foo' | should.any(should.be.a('number'), should.have.length.to(5))


def test_all_length_chain():
    'foo' | should.have.length.between.range(2, 5)
    ('foo'
        | should.have.length.lower.than(4)
        | should.have.length.higher.than(2))

    with pytest.raises(AssertionError):
        'foo' | should.have.length.lower.than(4) | should.have.length.higher(5)


def test_start_end_with():
    from collections import OrderedDict

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


def test_raises():
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


def test_pass_function():
    def test(subject):
        return len(subject) == 3, []

    'foo' | should.pass_test(test)
    'fo' | should.do_not.pass_test(test)

    with pytest.raises(AssertionError):
        'foo' | should.do_not.pass_test(test)


def test_implements():
    class foo(object):
        foo = None

        def bar():
            pass

        def baz():
            pass

    foo | should.implements.methods('bar', 'baz')
    foo | should.do_not.implements.methods('foo')

    with pytest.raises(AssertionError):
        foo | should.implement.methods('foo', 'faa')


def test_custom_message_error():
    with pytest.raises(AssertionError) as err:
        'foo' | should.be.equal('bar', msg='invalid string')
    str(err.value) | should.contain('invalid string')


def test_custom_error_message():
    # 'foo' | should.be.equal('bar', msg='invalid string')
    pass
