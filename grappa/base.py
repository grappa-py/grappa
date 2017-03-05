# -*- coding: utf-8 -*-
import functools


# List of unsupported binary operators
unsupported_operators = (
    # method    # operator symbol
    ('rshit',   '>>'),
    ('lshift',  '<<'),
    ('add',     '+'),
    ('and',     '&'),
)


def not_implemented(symbol, self, value):
    """
    Raises an `NotImplementedError` exception when called.
    """
    raise NotImplementedError('"{}" operator is not overloaded'.format(
        symbol
    ))


class BaseTest(object):
    """
    BaseTest implements magic method that explicitly raises an exception
    if consumed with unsupported binary operators.

    Note: methods are defined dynamically. See below.
    """


# Dynamically set class methods
for name, symbol in unsupported_operators:
    setattr(BaseTest, '__{}__'.format(name),
            functools.partial(not_implemented, symbol))
