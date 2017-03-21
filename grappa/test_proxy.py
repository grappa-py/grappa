# -*- coding: utf-8 -*-
import inspect
from .test import test


class TestProxy(object):
    """
    TestProxy acts like a delegator intermediate proxy between public
    API calls and `Test` instances defining the test style.

    Arguments:
        style (str): test style between `should` or `expect`.
    """

    def __init__(self, style):
        self._style = style

    def __getattr__(self, name):
        """
        Overloads object attribute accessory proxy to the currently used
        operator and parent test instance.
        """
        _test = getattr(test, name)

        if inspect.ismethod(_test):
            return _test

        _test._ctx.style = self._style
        return _test

    def __call__(self, *args, **kw):
        """
        Makes proxy object itself callable, delegating the invokation
        to a new test instance.
        """
        _test = test(*args, **kw)
        _test._ctx.style = self._style
        return _test
