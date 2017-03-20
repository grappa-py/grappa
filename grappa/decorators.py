# -*- coding: utf-8 -*-
import inspect
import functools
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
        _name = name if isinstance(name, str) else fn.__name__
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
