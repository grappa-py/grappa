# -*- coding: utf-8 -*-
from ..operator import Operator


class WithinOperator(Operator):
    """
    Asserts that a number is within a range.

    Example::

        # Should style
        4 | should.be.within(2, 5)
        5 | should.be.between(2, 5)
        4.5 | should.be.within(4, 5)

        # Should style - negation form
        4 | should.not_be.within(2, 5)
        5 | should.not_be.between(2, 5)
        4.5 | should.not_be.within(4, 5)

        # Expect style
        4 | expect.to.be.within(2, 5)
        5 | expect.to.be.between(2, 5)
        4.5 | expect.to.be.within(4, 5)

        # Expect style - negation form
        4 | expect.to_not.be.within(2, 5)
        5 | expect.to_not.be.between(2, 5)
        4.5 | expect.to_not.be.within(4, 5)
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('within', 'between')

    # Operator keywords
    aliases = ('to', 'numbers', 'range')

    # Expected template message
    expected_message = Operator.Dsl.Message(
        'a number that is within range {value}',
        'a number that is not within range {value}'
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an object of type "{type}" with value "{value}"',
    )

    def match(self, subject, start, end):
        if self.ctx.length:
            subject = len(subject)

        if not isinstance(subject, (int, float, complex)):
            return False, ['subject is not a numeric type']

        return start <= subject <= end, []
