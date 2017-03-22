# -*- coding: utf-8 -*-
import collections
from ..operator import Operator


class ContainOperator(Operator):
    """
    Asserts if a given value or values can be found
    in a another object.

    Example::

        # Should style
        'foo bar' | should.contain('bar')
        ['foo', 'bar'] | should.contain('bar')
        ['foo', 'bar'] | should.contain('foo', 'bar')
        [{'foo': True}, 'bar'] | should.contain({'foo': True})

        # Should style - negation form
        'foo bar' | should.do_not.contain('bar')
        ['foo', 'bar'] | should.do_not.contain('baz')

        # Expect style
        'foo bar' | expect.to.contain('bar')
        ['foo', 'bar'] | expect.to.contain('bar')
        ['foo', 'bar'] | expect.to.contain('foo', 'bar')
        [{'foo': True}, 'bar'] | expect.to.contain({'foo': True})

        # Expect style - negation form
        'foo bar' | expect.to_not.contain('bar')
        ['foo', 'bar'] | expect.to_not.contain('baz')
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Enable diff report
    show_diff = True

    # Operator keywords
    operators = ('contain', 'contains', 'includes')

    # Operator chain aliases
    aliases = ('value', 'item', 'string', 'text', 'expression', 'data')

    # Expected template message
    expected_message = Operator.Dsl.Message(
        'a value that contains "{value}"',
        'a value that does not contains "{value}"',
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an value of type "{type}" with content "{value}"',
    )

    # Stores types to normalize before the assertion
    NORMALIZE_TYPES = (
        collections.Iterator,
        collections.MappingView,
        collections.Set
    )

    def match(self, subject, *expected):
        if isinstance(subject, self.NORMALIZE_TYPES):
            subject = list(subject)

        if self._is_not_a_sequence(subject):
            return False, ['is not a valid sequence type']

        return self._matches(subject, *expected)

    def _is_not_a_sequence(self, value):
        return not isinstance(value, collections.Sequence)

    def _matches(self, subject, *expected):
        reasons = []

        for expected_item in expected:
            matches_any, reason = self._matches_any(expected_item, subject)
            reasons.append(reason)

            if not matches_any:
                return False, [reason]

        return True, reasons

    def _matches_any(self, expected, subject):
        if len(subject) == 0:
            return False, 'empty item'

        if isinstance(subject, str):
            if expected in subject:
                return True, 'item {0!r} found'.format(expected)
            return False, 'item {0!r} not found'.format(expected)

        for item in subject:
            if item == expected:
                return True, 'item {0!r} found'.format(expected)

        return False, 'item {0!r} not found'.format(expected)
