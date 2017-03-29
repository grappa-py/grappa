# -*- coding: utf-8 -*-
import collections

from ..operator import Operator
from ..constants import STR_TYPES


class StarEndBaseOpeartor(Operator):

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Chain aliases
    aliases = (
        'word', 'string', 'number', 'name', 'numbers', 'items',
        'value', 'char', 'letter', 'by', 'character', 'item',
    )

    def match(self, subject, *expected):
        if self.is_unordered_dict(subject):
            return False, ['does not have ordered keys']

        return self.matches(subject, *expected)

    def is_unordered_dict(self, subject):
        if isinstance(subject, collections.Mapping):
            if not hasattr(collections, 'OrderedDict'):
                return True
            return not isinstance(subject, collections.OrderedDict)
        return False


class StartWithOperator(StarEndBaseOpeartor):
    """
    Asserts if a given value starts with a specific items.

    Example::

        # Should style
        'foo' | should.start_with('f')
        'foo' | should.start_with('fo')
        [1, 2, 3] | should.start_with.number(1)
        iter([1, 2, 3]) | should.start_with.numbers(1, 2)
        OrderedDict([('foo', 0), ('bar', 1)]) | should.start_with.item('foo')

        # Should style - negation form
        'foo' | should.do_not.start_with('o')
        'foo' | should.do_not.start_with('o')
        [1, 2, 3] | should.do_not.start_with(2)
        iter([1, 2, 3]) | should.do_not.start_with.numbers(3, 4)
        OrderedDict([('foo', 0), ('bar', 1)]) | should.start_with('bar')

        # Expect style
        'foo' | expect.to.start_with('f')
        'foo' | expect.to.start_with('fo')
        [1, 2, 3] | expect.to.start_with.number(1)
        iter([1, 2, 3]) | expect.to.start_with.numbers(1, 2)
        OrderedDict([('foo', 0), ('bar', 1)]) | expect.to.start_with('foo')

        # Expect style - negation form
        'foo' | expect.to_not.start_with('f')
        'foo' | expect.to_not.start_with('fo')
        [1, 2, 3] | expect.to_not.start_with.number(1)
        iter([1, 2, 3]) | expect.to_not.start_with.numbers(1, 2)
        OrderedDict([('foo', 0), ('bar', 1)]) | expect.to_not.start_with('foo')
    """

    # Operator keywords
    operators = ('start_with', 'starts_with', 'startswith')

    # Expected template message
    expected_message = Operator.Dsl.Message(
        'an object that starts with items "{value}"',
        'an object that does not start with items "{value}"',
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an object of type "{type}" with value "{value}"',
    )

    def matches(self, subject, *expected):
        if isinstance(subject, STR_TYPES):
            return (
                subject.startswith(expected[0]),
                ['starts with {0!r}'.format(subject[:-len(expected[0])])])

        head = list(subject)[:len(expected)]
        return (
            list(expected) == head,
            ['starts with {0!r}'.format(head)])


class EndWithOperator(StarEndBaseOpeartor):
    """
    Asserts if a given value ends with a specific items.

    Example::

        # Should style
        'foo' | should.ends_with('o')
        'foo' | should.ends_with('oo')
        [1, 2, 3] | should.ends_with.number(3)
        iter([1, 2, 3]) | should.ends_with.numbers(2, 3)
        OrderedDict([('foo', 0), ('bar', 1)]) | should.ends_with.item('bar')

        # Should style - negation form
        'foo' | should.do_not.ends_with('f')
        'foo' | should.do_not.ends_with('o')
        [1, 2, 3] | should.do_not.ends_with(2)
        iter([1, 2, 3]) | should.do_not.ends_with.numbers(3, 4)
        OrderedDict([('foo', 0), ('bar', 1)]) | should.ends_with('foo')

        # Expect style
        'foo' | expect.to.ends_with('o')
        'foo' | expect.to.ends_with('oo')
        [1, 2, 3] | expect.to.ends_with.number(3)
        iter([1, 2, 3]) | expect.to.ends_with.numbers(2, 3)
        OrderedDict([('foo', 0), ('bar', 1)]) | expect.to.ends_with('bar')

        # Expect style - negation form
        'foo' | expect.to_not.ends_with('f')
        'foo' | expect.to_not.ends_with('oo')
        [1, 2, 3] | expect.to_not.ends_with.number(2)
        iter([1, 2, 3]) | expect.to_not.ends_with.numbers(1, 2)
        OrderedDict([('foo', 0), ('bar', 1)]) | expect.to_not.ends_with('foo')
    """

    # Operator keywords
    operators = ('end_with', 'ends_with', 'endswith')

    # Expected template message
    expected_message = Operator.Dsl.Message(
        'an object that ends with items "{value}"',
        'an object that does not end with items "{value}"',
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an object of type "{type}" with value "{value}"',
    )

    def matches(self, subject, *expected):
        if isinstance(subject, STR_TYPES):
            return (
                subject.endswith(expected[0]),
                ['ends with {0!r}'.format(subject[-len(expected[0]):])])

        tail = list(subject)[-len(expected):]
        return (
            list(expected) == tail,
            ['ends with {0!r}'.format(tail)])
