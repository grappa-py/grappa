# -*- coding: utf-8 -*-
from ..operator import Operator

from .been_called import mock_implementation_validator

class BeenCalledWithOperator(Operator):
    """
    Asserts whether a mock have been called with arguments or not.
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

    @mock_implementation_validator
    def match(self, subject, *args):
        try:
            subject.assert_called_with(*args)
            return True
        except AssertionError as error:
            return False, [ error.args[0] ]


class BeenCalledOnceWithOperator(Operator):
    """
    Asserts whether a mock have been called once with arguments or not.
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('been_called_once_with',)

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a mock that has been called once with arguments',
        'a mock that has not been called once with arguments',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a mock that has been called {call_count} time(s) with arguments',
        'a mock that has been called once with arguments',
    )

    @mock_implementation_validator
    def match(self, subject, *args):
        try:
            subject.assert_called_once_with(*args)
            return True
        except AssertionError as error:
            return False, [ error.args[0] ]
