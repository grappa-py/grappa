# -*- coding: utf-8 -*-

# Import test module
from .test import Test
# Import test proxy used for style delegation
from .test_proxy import TestProxy
# Expose plugin module as part of the public API
from .plugin import use
# Expose config module as part of the public API
from .config import config
# Expose decorator for operators factory
from .decorators import *  # noqa
# Expose Operatocdr base class
from .operator import Operator
# Required to load built-in operators
from . import operators

# Initialize colorama stdout/stderr interceptor
import colorama
colorama.init()

# IMPORTANT! Autoload built-in operators
operators.load()

# Global test instance for "should" testing declaration style
should = TestProxy('should')

# Global test instance for "expect" testing declaration style
expect = TestProxy('expect')

# Module symbols to export as public API
__all__ = (
    'should',
    'expect',
    'Test',
    'use',
    'config',
    'Operator',
    'attribute',
    'operator',
    'register'
)
