# -*- coding: utf-8 -*-
from ..operator import Operator


class BelowOperator(Operator):
    """
    Asserts if a given number is below to another number.

    Example::

        # Should style
        3 | should.be.below(5)
        3 | should.be.below.of(5)
        3 | should.be.below.to(5)
        3 | should.be.less.than(5)
        3 | should.be.lower.than(5)
        3 | should.be.below.to.number(5)
        3 | should.be.below.than.number(5)

        # Should style - negation form
        5 | should.not_be.below(3)
        5 | should.not_be.below.of(3)
        3 | should.not_be.below.to(5)
        3 | should.not_be.lower.than(5)
        5 | should.not_be.below.to.number(3)

        # Expect style
        3 | expect.to.be.below(5)
        3 | expect.to.be.below.of(5)
        3 | expect.to.be.below.to(5)
        3 | expect.to.be.less.than(5)
        3 | expect.to.be.lower.than(5)
        3 | expect.to.be.below.to.number(5)
        3 | expect.to.be.below.than.number(5)

        # Expect style - negation form
        5 | expect.to_not.be.below(3)
        5 | expect.to_not.be.below.of(3)
        5 | expect.to_not.be.below.than(3)
        5 | expect.to_not.be.below.to.number(3)
        5 | expect.to_not.be.below.than.number(3)
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('below', 'lower', 'less')

    # Operator keywords
    aliases = ('of', 'to', 'number', 'than')

    # Expected template message
    expected_message = Operator.Dsl.Message(
        'a number that is below to {value}',
        'a number that is not below to {value}'
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an object of type "{type}" with value "{value}"',
    )

    def match(self, subject, expected):
        if self.ctx.length:
            subject = len(subject)

        if not isinstance(subject, (int, float, complex)):
            return False, ['subject is not a numeric type']

        return subject < expected, ['subject is not lower than {expected}']


class AboveOperator(BelowOperator):
    """
    Asserts if a given number is above to another number.

    Example::

        # Should style
        5 | should.be.above(3)
        5 | should.be.above.of(3)
        5 | should.be.above.to(3)
        5 | should.be.higher.than(3)
        5 | should.be.above.to.number(3)
        5 | should.be.above.than.number(3)

        # Should style - negation form
        3 | should.not_be.above(5)
        3 | should.not_be.above.of(5)
        3 | should.not_be.above.to(5)
        3 | should.not_be.higher.than(5)
        3 | should.not_be.above.to.number(5)
        3 | should.not_be.above.than.number(5)

        # Expect style
        5 | expect.to.be.above(3)
        5 | expect.to.be.above.of(3)
        5 | expect.to.be.above.to(3)
        5 | expect.to.be.higher.than(3)
        5 | expect.to.be.above.to.number(3)
        5 | expect.to.be.above.than.number(3)

        # Expect style - negation form
        3 | expect.not_to.be.above(5)
        3 | expect.not_to.be.above.of(5)
        3 | expect.not_to.be.above.to(5)
        3 | expect.not_to.be.higher.than(5)
        3 | expect.not_to.be.above.to.number(5)
        3 | expect.not_to.be.above.than.number(5)
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('above', 'higher')

    # Expected
    expected = 'a "True" boolean value'

    # Expected template message
    expected_message = Operator.Dsl.Message(
        'a number that is above to {value}',
        'a number that is not above to {value}'
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an object of type "{type}" with value "{value}"',
    )

    def match(self, subject, expected):
        if self.ctx.length and not isinstance(subject, (int, float)):
            subject = len(subject)

        if not isinstance(subject, (int, float, complex)):
            return False, ['subject is not a numeric type']

        return subject > expected, []


class AboveOrEqualOperator(BelowOperator):
    """
    Asserts if a given number is above or equal to another number.

    Example::

        # Should style
        3 | should.be.least(3)
        3 | should.be.above_or_equal(3)
        3 | should.be.above_or_equal.of(3)
        3 | should.be.above_or_equal.to(3)
        3 | should.be.higher_or_equal.than(3)
        3 | should.be.above_or_equal.to.number(3)
        3 | should.be.above_or_equal.than.number(3)

        # Should style - negation form
        3 | should.not_be.least(3)
        3 | should.not_be.above_or_equal(5)
        3 | should.not_be.above_or_equal.of(5)
        3 | should.not_be.above_or_equal.to(5)
        3 | should.not_be.higher_or_equal.than(5)
        3 | should.not_be.higher_or_equal.to.number(5)
        3 | should.not_be.higher_or_equal.than.number(5)

        # Expect style
        3 | expect.to.be.least(3)
        3 | expect.to.be.above_or_equal(3)
        3 | expect.to.be.above_or_equal.of(3)
        3 | expect.to.be.above_or_equal.to(3)
        3 | expect.to.be.higher_or_equal.than(3)
        3 | expect.to.be.above_or_equal.to.number(3)
        3 | expect.to.be.above_or_equal.than.number(3)

        # Expect style - negation form
        3 | expect.not_be.least(3)
        3 | expect.not_be.above_or_equal(5)
        3 | expect.not_be.above_or_equal.of(5)
        3 | expect.not_be.above_or_equal.to(5)
        3 | expect.not_be.higher_or_equal.than(5)
        3 | expect.not_be.higher_or_equal.to.number(5)
        3 | expect.not_be.higher_or_equal.than.number(5)
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('above_or_equal', 'higher_or_equal', 'least')

    # Expected
    expected = 'a "True" boolean value'

    # Expected template message
    expected_message = Operator.Dsl.Message(
        'a number that is higher or equal to {value}',
        'a number that is not higher or equal to {value}'
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an object of type "{type}" with value "{value}"',
    )

    def match(self, subject, expected):
        if self.ctx.length:
            subject = len(subject)

        if not isinstance(subject, (int, float, complex)):
            return False, ['subject is not a numeric type']

        return subject >= expected, []


class BelowOrEqualOperator(BelowOperator):
    """
    Asserts if a given number is below or equal to another number.

    Example::

        # Should style
        3 | should.be.most(3)
        3 | should.be.below_or_equal(3)
        3 | should.be.below_or_equal.of(3)
        3 | should.be.below_or_equal.to(3)
        3 | should.be.lower_or_equal.than(3)
        3 | should.be.lower_or_equal.to.number(3)
        3 | should.be.lower_or_equal.than.number(3)

        # Should style - negation form
        3 | should.not_be.most(5)
        3 | should.not_be.below_or_equal(5)
        3 | should.not_be.below_or_equal.of(5)
        3 | should.not_be.below_or_equal.to(5)
        3 | should.not_be.lower_or_equal.than(5)
        3 | should.not_be.lower_or_equal.to.number(5)
        3 | should.not_be.lower_or_equal.than.number(5)

        # Expect style
        3 | expect.to.be.most(3)
        3 | expect.to.be.below_or_equal(3)
        3 | expect.to.be.below_or_equal.of(3)
        3 | expect.to.be.below_or_equal.to(3)
        3 | expect.to.be.lower_or_equal.than(3)
        3 | expect.to.be.lower_or_equal.to.number(3)
        3 | expect.to.be.lower_or_equal.than.number(3)

        # Expect style - negation form
        3 | expect.not_be.most(5)
        3 | expect.not_be.below_or_equal(5)
        3 | expect.not_be.below_or_equal.of(5)
        3 | expect.not_be.below_or_equal.to(5)
        3 | expect.not_be.lower_or_equal.than(5)
        3 | expect.not_be.lower_or_equal.to.number(5)
        3 | expect.not_be.lower_or_equal.than.number(5)
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('below_or_equal', 'lower_or_equal', 'most')

    # Expected
    expected = 'a "True" boolean value'

    # Expected template message
    expected_message = Operator.Dsl.Message(
        'a number that is below or equal to {value}',
        'a number that is not below or equal to {value}'
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an object of type "{type}" with value "{value}"',
    )

    def match(self, subject, expected):
        if self.ctx.length:
            subject = len(subject)

        if not isinstance(subject, (int, float, complex)):
            return False, ['subject is not a numeric type']

        return subject <= expected, []
