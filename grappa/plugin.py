# -*- coding: utf-8 -*-
import inspect

from .log import log
from .engine import Engine


def use(plugin):
    """
    Register plugin in grappa.

    `plugin` argument can be a function or a object that implement `register`
    method, which should accept one argument: `grappa.Engine` instance.

    Arguments:
        plugin (function|module): grappa plugin object to register.

    Raises:
        ValueError: if `plugin` is not a valid interface.

    Example::

        import grappa

        class MyOperator(grappa.Operator):
            pass

        def my_plugin(engine):
            engine.register(MyOperator)

        grappa.use(my_plugin)
    """
    log.debug('register new plugin: {}'.format(plugin))

    if inspect.isfunction(plugin):
        return plugin(Engine)

    if plugin and hasattr(plugin, 'register'):
        return plugin.register(Engine)

    raise ValueError('invalid plugin: must be a function or '
                     'implement register() method')
