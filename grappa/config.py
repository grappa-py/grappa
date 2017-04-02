# -*- coding: utf-8 -*-
import logging
import functools

from .log import log


def validate(method):
    """
    Config option name value validator decorator.
    """
    # Name error template
    name_error = 'configuration option "{}" is not supported'

    @functools.wraps(method)
    def validator(self, name, *args):
        if name not in self.allowed_opts:
            raise ValueError(name_error.format(name))
        return method(self, name, *args)
    return validator


class Config(object):
    """
    Config provides a simple key-value Pythonic data store for grappa
    runtime configuration settings.
    """

    # Default options store
    defaults = {
        # Debug enables internal logging. Defaults to False.
        'debug': False,
        # show_code enables/disables code output in errors.
        'show_code': True,
        # colors enables/disables colored ANSI sequences for the terminal
        'use_colors': True
    }

    # List of supported configuration names
    allowed_opts = defaults.keys()

    def __init__(self):
        self.__dict__['opts'] = self.defaults.copy()

    @validate
    def __getattr__(self, name):
        return self.opts.get(name)

    @validate
    def __setattr__(self, name, value):
        self.opts[name] = value

        # Configure logger level
        if name == 'debug':
            log.setLevel(logging.DEBUG if value is True
                         else logging.CRITICAL)

        log.debug('[config] set option {}="{}"'.format(name, value))


# Global config store
config = Config()
