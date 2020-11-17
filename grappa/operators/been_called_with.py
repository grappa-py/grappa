# -*- coding: utf-8 -*-
from ..operator import Operator

class BeenCalledWithOperator(Operator):
    """
    Asserts whether a MagicMock have been called with arguments or not.
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('been_called_with',)

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a mock that has been called at least once with arguments',
        'a mock that has not been called with arguments',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a mock that has not been called with arguments',
        'a mock that has been called at least once with arguments',
    )

    def match(self, subject, *args):
        if subject.__class__.__name__ == 'MagicMock':
            try:
                subject.assert_called_with(*args)
                return True
            except AssertionError as error:
                return False, [ error.args[0] ]

        return False, ['subject is not a MagicMock patch but a ' + subject.__class__.__name__]


class BeenCalledOnceWithOperator(Operator):
    """
    Asserts whether a MagicMock have been called once with arguments or not.
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('been_called_once_with',)

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a mock that has been called only one time with arguments',
        'a mock that has not been called or has been called more than one time with arguments',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a mock that has not been called or has been called more than one time with arguments',
        'a mock that has been called only one time with arguments',
    )

    def match(self, subject, *args):
        if subject.__class__.__name__ == 'MagicMock':
            try:
                subject.assert_called_once_with(*args)
                return True
            except AssertionError as error:
                return False, [ error.args[0] ]

        return False, ['subject is not a MagicMock patch but a ' + subject.__class__.__name__]

