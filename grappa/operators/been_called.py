# -*- coding: utf-8 -*-
from ..decorators import mock_implementation_validator
from ..operator import Operator


class BeenCalledOperator(Operator):
    """
    Asserts whether a mock have been called or not.
    """

    # Is the operator a keyword
    kind = Operator.Type.ACCESSOR

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('been_called',)

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a mock that has been called at least once',
        'a mock that has not been called',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a mock that has not been called',
        'a mock that has been called at least once',
    )

    @mock_implementation_validator
    def match(self, subject):
        return subject.called


class BeenCalledOnceOperator(Operator):
    """
    Asserts whether a mock have been called once or not.
    """

    # Is the operator a keyword
    kind = Operator.Type.ACCESSOR

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('been_called_once',)

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a mock that has been called once',
        'a mock that has not been called once',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a mock that has been called {call_count} time(s)',
        'a mock that has been called once',
    )

    @mock_implementation_validator
    def match(self, subject):
        return subject.call_count == 1


class BeenCalledTimesOperator(Operator):
    """
    Asserts whether a mock have been called X times or not.
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Disable diff report
    show_diff = True

    # Operator keywords
    operators = ('been_called_times',)

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a mock that has been called {value} times',
        'a mock that has not been called {value} times',
    )

    subject_message = Operator.Dsl.Message(
        'a mock that has been called {call_count} times',
        'a mock that has not been called {call_count} times',
    )

    @mock_implementation_validator
    def match(self, subject, expected):
        return subject.call_count == expected
