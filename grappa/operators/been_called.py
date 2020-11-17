# -*- coding: utf-8 -*-
import functools

from ..operator import Operator
from ..api import TestProxy

def mock_implementation_validator(func):
    @functools.wraps(func)
    def wrapper(operator, subject, *args, **kwargs):
        expect = TestProxy('expect')

        def validate_properties(reasons, prop):
            try:
                expect(subject).to.have.property(prop)
            except AssertionError:
                reasons.append('a property named "{}" is expected'.format(prop))
            return reasons

        def validate_methods(reasons, method):
            try:
                expect(subject).to.implement.methods(method)
            except AssertionError:
                reasons.append('a method named "{}" is expected'.format(method))
            return reasons

        expected_properties = ('called', 'call_count')
        reasons = functools.reduce(validate_properties, expected_properties, [])

        expected_methods = ('assert_called_with', 'assert_called_once_with')
        reasons = functools.reduce(validate_methods, expected_methods, reasons)

        if reasons:
            reasons.insert(0, 'mock implementation is incomplete')
            return False, reasons
        
        return func(operator, subject, *args, **kwargs)

    return wrapper


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
