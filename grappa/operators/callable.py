# -*- coding: utf-8 -*-
from ..operator import Operator


class CallableOperator(Operator):
    """
    Asserts if a given subject is a callable type or an object that
    implements ``__call__()`` magic method.

    Example::

        # Should style
        (lambda x: x) | should.be.callable

        # Should style - negation form
        None | should.not_be.callable

        # Expect style
        (lambda x: x) | expect.to.be.callable

        # Expect style - negation form
        None | expect.to_not.be.callable
    """

    # Is the operator a keyword
    kind = Operator.Type.ACCESSOR

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('callable',)

    # Expected template message
    expected_message = Operator.Dsl.Message(
        'a callable object, such as a function or method',
        'a non callable object, such as a function or method'
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an object which is a "{type}" type'
    )

    # Assertion information
    information = (
        Operator.Dsl.Help(
            Operator.Dsl.Description(
                'Callable objects can be tested via "callable(x)" Python',
                'built-in function.'
            ),
            Operator.Dsl.Reference(
                'https://docs.python.org/3/library/functions.html#callable'
            ),
        ),
        Operator.Dsl.Help(
            Operator.Dsl.Description(
                'Callable objects in Python are functions, methods, classes,',
                'or any other object that implements "__call__()" method.'
            ),
            Operator.Dsl.Reference(
                'http://stackoverflow.com/a/2436614'
            ),
        ),
    )

    def match(self, value):
        if value is None:
            return False, ['a callable value cannot be "None"']

        # Custom expectations messages
        self.expected = 'an callable object, such as a function or method'
        self.value = value

        return callable(value), []
