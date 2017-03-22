# -*- coding: utf-8 -*-
from ..operator import Operator


class NoneOperator(Operator):
    """
    Asserts if a given subject is ``None``.

    Example::

        # Should style
        None | should.be.none

        # Should style - negation form
        'foo' | should.not_be.none

        # Expect style
        None | expect.to.be.none

        # Expect style - negation form
        'foo' | expect.to_not.be.none
    """

    # Is the operator a keyword
    kind = Operator.Type.ACCESSOR

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('none',)

    # Disable chanined calls
    chainable = False

    # Expected message templates
    expected_message = Operator.Dsl.Message(
        'a value that is exactly equal to "None"',
        'a value that is not equal to "None"',
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an object with type "{type}" with value "{value}"',
    )

    # Assertion information
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

    def match(self, subject):
        return subject is None, []
