from .base import BaseTest


class AssertionProxy(BaseTest):
    """
    AssertionProxy is used as proxy delegator call chain for test
    definitions.
    """

    def __init__(self, test, operator, fn):
        self._fn = fn
        self._test = test
        self._op = operator

    def __call__(self, expected, *args, **kw):
        return self._fn(expected, *args, **kw)

    def __getattr__(self, name):
        # Match chain aliases
        if hasattr(self._op, 'aliases') and name in self._op.aliases:
            self._test._engine.add_keyword(name)
            return self

        # Fallback to parent assertion object
        return getattr(self._test, name)

    def __ror__(self, value):
        """
        Overloads ``|`` operator.
        """
        return self._fn(value)._trigger()

    def __gt__(self, value):
        """
        Overloads ``>`` operator.
        """
        return self.__ror_(value)
