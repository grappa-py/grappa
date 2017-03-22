# -*- coding: utf-8 -*-
from ..operator import Operator


class PresentOperator(Operator):
    """
    Asserts if a given subject is not ``None`` or a negative value
    if evaluated via logical unary operator.

    This operator is the opposite of ``empty``.

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

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('present', 'exists')

    # Expected
    expected = 'a value which is not None and has data'

    # Expected template message
    expected_message = Operator.Dsl.Message(
        'a value that is not None and its length is not "0"',
        'a value that is None or its length is "0"'
    )

    # Assertion information
    information = (
        Operator.Dsl.Help(
            Operator.Dsl.Description(
                'An present object is the oposite of an empty object.'
            )
        ),
    )

    def match(self, subject):
        if subject is None:
            return False, ['subject is "None"']

        return bool(subject is not None and subject), []
