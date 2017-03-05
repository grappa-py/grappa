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

    # Operator keywords
    operators = ('contain', 'contains', 'includes')

    # Operaror chain aliases
    aliases = ('value', 'item', 'string', 'text', 'expression', 'data')

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a value that contains "{value}"',
        'a value that does not contains "{value}"',
    )
    subject_message = Operator.Dsl.Message(
        'an value of type "{type}" with content "{value}"',
    )

    def after_error(self, error, value, expected=None):
        pass

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

            if not matches_any:
                return False, [reason]
            else:
                reasons.append(reason)

        return True, reasons

    def _matches_any(self, expected, subject):
        if len(subject) == 0:
            return False, 'is empty'

        if isinstance(subject, str):
            if expected in subject:
                return True, 'item {0!r} found'.format(expected)
            return False, 'item {0!r} not found'.format(expected)

        # expected = default_matcher(expected)
        for item in subject:
            matches, _ = expected._match(item)
            if matches:
                return True, 'item {0!r} found'.format(expected)

        return False, 'item {0!r} not found'.format(expected)
