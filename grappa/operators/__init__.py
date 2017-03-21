# -*- coding: utf-8 -*-
from ..engine import Engine

# Module symbols to export
__all__ = ('operators', 'load')


# List of built-in operators
operators = (
    # Module name   # Operator class to import
    ('attributes', ),
    ('type',        'TypeOperator'),
    ('none',        'NoneOperator'),
    ('keys',        'KeysOperator'),
    ('index',       'IndexOperator'),
    ('match',       'MatchOperator'),
    ('length',      'LengthOperator'),
    ('empty',       'EmptyOperator'),
    ('equal',       'EqualOperator'),
    ('within',      'WithinOperator'),
    ('present',     'PresentOperator'),
    ('contain',     'ContainOperator'),
    ('callable',    'CallableOperator'),
    ('property',    'PropertyOperator'),
    ('pass_test',   'PassTestOperator'),
    ('implements',  'ImplementsOperator'),
    ('raises',      'RaisesOperator'),

    ('bool',        'TrueOperator', 'FalseOperator'),
    ('start_end',   'StartWithOperator', 'EndWithOperator'),

    ('range',       'BelowOperator', 'AboveOperator',
                    'AboveOrEqualOperator', 'BelowOrEqualOperator'),
)


def load():
    """
    Loads the built-in operators into the global test engine.
    """
    for operator in operators:
        module, symbols = operator[0], operator[1:]
        path = 'grappa.operators.{}'.format(module)

        # Dynamically import modules
        operator = __import__(path, None, None, symbols)

        # Register operators in the test engine
        for symbol in symbols:
            Engine.register(getattr(operator, symbol))
