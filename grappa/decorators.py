# -*- coding: utf-8 -*-
import inspect
import functools
import six
from .api import TestProxy
from .engine import Engine
from .operator import Operator


# Explicit module members to export
__all__ = (
    'operator',
    'attribute',
    'register'
)


def operator(name=None, operators=None, aliases=None, kind=None):
    """
    Registers a new operator function in the test engine.

    Arguments:
        *args: variadic arguments.
        **kw: variadic keyword arguments.

    Returns:
        function
    """
    def delegator(assertion, subject, expected, *args, **kw):
        return assertion.test(subject, expected, *args, **kw)

    def decorator(fn):
        operator = Operator(fn=fn, aliases=aliases, kind=kind)
        _name = name if isinstance(name, six.string_types) else fn.__name__
        operator.operators = (_name,)

        _operators = operators
        if isinstance(_operators, list):
            _operators = tuple(_operators)

        if isinstance(_operators, tuple):
            operator.operators += _operators

        # Register operator
        Engine.register(operator)
        return functools.partial(delegator, operator)

    return decorator(name) if inspect.isfunction(name) else decorator


def attribute(*args, **kw):
    """
    Registers a new attribute only operator function in the test engine.

    Arguments:
        *args: variadic arguments.
        **kw: variadic keyword arguments.

    Returns:
        function
    """
    return operator(kind=Operator.Type.ATTRIBUTE, *args, **kw)


def register(operator):
    """
    Registers a new operator class in the test engine.

    Arguments:
        operator (Operator): operator class to register.

    Returns:
        Operator: operator class.
    """
    Engine.register(operator)
    return operator


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