from ..operator import Operator


class PresentOperator(Operator):
    """
    Asserts if a given subject is not ``None`` or a negative value
    if evaluated via logical unary operator.

    Example::

        # Should style
        'foo' | should.be.present

        # Should style - negation form
        '' | should.not_be.present

        # Expect style
        'foo' | expect.to.be.present

        # Expect style - negation form
        False | expect.to_not.be.present
    """

    # Is the operator a keyword
    kind = Operator.Type.ACCESSOR

    # Operator keywords
    operators = ('present', 'exists')

    # Expected
    expected = 'a value which is not None and has data'

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a "True" value'
    )

    subject_message = Operator.Dsl.Message(
        'a "True" value',
        'a value which is not "True"',
    )

    information = (
        Operator.Dsl.Help(
            Operator.Dsl.Description(
                'An empty object is typically tested via "len(x)"',
                'built-in function. Most built-in types and objects in Python',
                'can be tested that way, such as str, list, generator...',
                'as well as any object that implements "__len__()" method',
                'and returns "0" as length.'
            ),
            Operator.Dsl.Reference(
                'https://docs.python.org/3/library/functions.html#len'
            ),
        ),
    )

    def match(self, subject):
        if subject is None:
            return False, ['subject is "None"']

        return bool(subject is not None and subject), []
