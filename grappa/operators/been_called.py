# -*- coding: utf-8 -*-
from ..operator import Operator


class BeenCalledOperator(Operator):
    """
    Asserts whether a MagicMock have been called or not.
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

    def match(self, subject):
        if subject.__class__.__name__ == 'MagicMock':
            return subject.called

        return False, ['subject is not a MagicMock patch but a ' + subject.__class__.__name__]


class BeenCalledOnceOperator(Operator):
    """
    Asserts whether a MagicMock have been called once or not.
    """

    # Is the operator a keyword
    kind = Operator.Type.ACCESSOR

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('been_called_once',)

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a mock that has been called only one time',
        'a mock that has not been called or has been called more than one time',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a mock that has not been called or has been called more than one time',
        'a mock that has been called only one time',
    )

    def match(self, subject):
        if subject.__class__.__name__ == 'MagicMock':
            return subject.call_count == 1

        return False, ['subject is not a MagicMock patch but a ' + subject.__class__.__name__]


class BeenCalledTimesOperator(Operator):
    """
    Asserts whether a MagicMock have been called X times or not.
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

    def match(self, subject, expected):
        if subject.__class__.__name__ == 'MagicMock':
            return subject.call_count == expected

        return False, ['subject is not a MagicMock patch but a ' + subject.__class__.__name__]
