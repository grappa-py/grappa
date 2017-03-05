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

    # Operator keywords
    operators = ('within', 'between')

    # Operator keywords
    aliases = ('to', 'numbers', 'range')

    # Expected
    expected = 'a "True" boolean value'

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a number value'
    )

    subject_message = Operator.Dsl.Message(
        'a "True" value',
        'a value which is not "True"',
    )

    def match(self, subject, start, end):
        if self.ctx.length:
            subject = len(subject)

        if not isinstance(subject, (int, float, complex)):
            return False, ['subject is not a numeric type']

        return start <= subject <= end, []
