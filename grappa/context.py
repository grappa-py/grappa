# -*- coding: utf-8 -*-


class Context(object):
    """
    Context is used to keep state and share data across test operators.

    Context typically stores operator defined flags that are accessed later
    by other operators in order to retrieve information or modify its
    evaluation behavior.

    From test runner perspective, a new context is created on every
    assertion execution phase, so context data is context-dependent of
    the testing scope.

    Attributes:
        flags (dict): stores context shared data by flag name.

    Example::

        from grappa.context import Context

        ctx = Context()

        ctx.negate = True

        if ctx.has('negate'):
            ctx.negate = False
            ctx.value = 'foo'

        ctx.negate # => False
        ctx.value # => 'foo'
    """

    def __init__(self, defaults=None, **kw):
        self.__dict__['flags'] = defaults or {'negate': False}

        for name, value in kw.items():
            self.__dict__['flags'][name] = value

    def has(self, flag):
        """
        Returns `True` if the given flag name is present in the current
        context instance.

        Returns:
            bool
        """
        return flag in self.flags

    def __getattr__(self, name):
        """
        Overloads class attribute accessor method in order to proxy access to
        the store.
        """
        return self.flags.get(name)

    def __setattr__(self, name, value):
        """
        Overloads class set attribute method in order to proxy access to the
        store.
        """
        self.flags[name] = value

    def clone(self):
        """
        Returns a copy of the current `Context` instance.

        Returns:
            grappa.Context
        """
        return Context(self.__dict__['flags'].copy())

    def __repr__(self):
        """
        Human-readable context data.

        Returns:
            str
        """
        return str(self.__dict__['flags'])
