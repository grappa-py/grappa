# -*- coding: utf-8 -*-
from .runner import Runner


def isoperator(x):
    """
    Returns `True` if the given object implements the required attributes for
    an operator.

    Returns:
        bool
    """
    return all(
        hasattr(x, name) for name in ('run', 'operators', 'kind', '__class__')
    )


def register_operators(*operators):
    """
    Registers one or multiple operators in the test engine.
    """
    def validate(operator):
        if isoperator(operator):
            return True

        raise NotImplementedError('invalid operator: {}'.format(operator))

    def register(operator):
        # Register operator by DSL keywords
        for name in operator.operators:
            # Check valid operators
            if name in Engine.operators:
                raise ValueError('operator name "{}" from {} is already '
                                 'in use by other operator'.format(
                                    name,
                                    operator.__name__
                                 ))

            # Register operator by name
            Engine.operators[name] = operator

    # Validates and registers operators
    [register(operator) for operator in operators if validate(operator)]


class Engine(object):
    """
    Engine implements the test engine responsible of registering, storing and
    running test operators.
    """

    # globally store test operators by name
    operators = {}

    def __init__(self):
        self.keywords = []
        self.assertions = []

    @staticmethod
    def register(*operators):
        """
        Registers one or multiple operators in the test engine.
        """
        register_operators(*operators)

    @property
    def empty(self):
        return len(self.assertions) == 0

    def add_assertion(self, assertion):
        self.assertions.append(assertion)

    def add_keyword(self, keyword):
        self.keywords.append(keyword)

    def reverse(self):
        self.assertions.reverse()

    def find_operator(self, name):
        return self.operators.get(name)

    def run(self, ctx):
        return Runner(self).run(ctx)

    def reset(self):
        self.__init__()

    def reset_keywords(self):
        self.keywords = []

    def clone(self):
        engine = Engine()
        engine.keywords = self.keywords[:]
        engine.assertions = self.assertions[:]
        return engine
