from ..operator import Operator


class EqualOperator(Operator):
    """
    Performs a strict equality comparison between ``x`` and ``y`` values.

    Uses ``==`` built-in binary operator for the comparison.

    Example::

        # Should style
        'foo' | should.be.equal('foo')
        'foo' | should.be.equal.to('foo')
        'foo' | should.be.equal.to.value('foo')

        # Should style - negation form
        'foo' | should.not_be.equal('foo')
        'foo' | should.not_be.equal.to('foo')
        'foo' | should.not_be.equal.to.value('foo')

        # Expect style
        'foo' | expect.to.equal('foo')
        'foo' | expect.to.equal.to('foo')
        'foo' | expect.to.equal.to.value('foo')

        # Expect style - negation form
        'foo' | expect.to_not.equal('foo')
        'foo' | expect.to_not.equal.to('foo')
        'foo' | expect.to_not.equal.to.value('foo')
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('equal', 'same')

    # Operaror chain aliases
    aliases = ('value', 'data', 'to', 'of', 'as')

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a value that is equal to "{value}"',
        'a value that is not equal to "{value}"',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'an value of type "{type}" with data "{value}"',
    )

    information = (
        Operator.Dsl.Help(
            Operator.Dsl.Description(
                '"None" is a built-in constant in Python that represents the',
                'absence of a value, as when default arguments are not passed',
                'to a function. The sole value of the type NoneType.',
            ),
            Operator.Dsl.Reference(
                'https://docs.python.org/3/library/constants.html#None'
            ),
        ),
    )

    def match(self, subject, expected):
        return subject == expected, []
