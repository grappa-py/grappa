# -*- coding: utf-8 -*-
import types
import inspect
from array import array

from ..operator import Operator

# Type alias mappings
MAPPINGS = {
    'string': str,
    'int': int,
    'integer': int,
    'number': int,
    'object': object,
    'float': float,
    'bool': bool,
    'boolean': bool,
    'complex': complex,
    'list': list,
    'dict': dict,
    'dictionary': dict,
    'tuple': tuple,
    'set': set,
    'array': array,
    'lambda': types.LambdaType,
    'generator': types.GeneratorType,
    'asyncgenerator': getattr(types, 'GeneratorType', None),
    'class': 'class',
    'method': 'method',
    'module': 'module',
    'function': 'function',
    'coroutine': 'coroutine',
    'generatorfunction': 'generatorfunction',
    'generator function': 'generatorfunction',
    'coroutinefunction': 'coroutinefunction',
}


class TypeOperator(Operator):
    """
    Asserts if a given object satisfies a type.

    You can use both a type alias string or a ``type`` object.

    Example::

        # Should style
        1 | should.be.an('int')
        1 | should.be.an('number')
        True | should.be.a('bool')
        True | should.be.type(bool)
        'foo' | should.be.a(str)
        'foo' | should.be.a('string')
        [1, 2, 3] | should.be.a('list')
        [1, 2, 3] | should.have.type.of(list)
        (1, 2, 3) | should.be.a('tuple')
        (1, 2, 3) | should.have.type.of(tuple)
        (lamdba x: x) | should.be.a('lambda')
        'foo' | should.be.instance.of('string')

        # Should style - negation form
        1 | should.not_be.an('int')
        1 | should.not_be.an('number')
        True | should.not_be.a('bool')
        True | should.not_be.type(bool)
        'foo' | should.not_be.a(str)
        'foo' | should.not_be.a('string')
        [1, 2, 3] | should.not_be.a('list')
        [1, 2, 3] | should.have_not.type.of(list)
        (1, 2, 3) | should.not_be.a('tuple')
        (1, 2, 3) | should.have_not.type.of(tuple)
        (lamdba x: x) | should.not_be.a('lambda')

        # Expect style
        1 | expect.to.be.an('int')
        1 | expect.to.be.an('number')
        True | expect.to.be.a('bool')
        True | expect.to.be.type(bool)
        'foo' | expect.to.be.a(str)
        'foo' | expect.to.be.a('string')
        [1, 2, 3] | expect.to.be.a('list')
        [1, 2, 3] | expect.to.have.type.of(list)
        (1, 2, 3) | expect.to.be.a('tuple')
        (1, 2, 3) | expect.to.have.type.of(tuple)
        (lamdba x: x) | expect.to.be.a('lambda')
        'foo' | expect.to.be.instance.of('string')

        # Expect style - negation form
        1 | expect.to_not.be.an('int')
        1 | expect.to_not.be.an('number')
        True | expect.to_not.be.a('bool')
        True | expect.to_not.be.type(bool)
        'foo' | expect.to_not.be.a(str)
        'foo' | expect.to_not.be.a('string')
        [1, 2, 3] | expect.to_not.be.a('list')
        [1, 2, 3] | expect.to_not.have.type.of(list)
        (1, 2, 3) | expect.to_not.be.a('tuple')
        (1, 2, 3) | expect.to_not.have.type.of(tuple)
        (lamdba x: x) | expect.to_not.be.a('lambda')
        'foo' | expect.to_not.be.instance.of('string')
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('type', 'types', 'a', 'an', 'instance')

    # Operator chain aliases
    aliases = ('type', 'types', 'of', 'equal', 'to')

    # Subject message template
    expected_message = Operator.Dsl.Message(
        'an object that is a "{value}" type',
        'an object that is not a "{value}" type'
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an object of type "{type}" with value "{value}"'
    )

    def match(self, value, expected):
        # Custom expectations yielded values
        self.value = type(value).__name__
        self.expected = expected

        # Get type alias
        if type(expected) is str:
            self.expected = expected
            _expected = MAPPINGS.get(expected)

            # Overwrite type value string
            self.expected = _expected

            if not _expected:
                raise ValueError('unsupported type alias: {}'.format(expected))

            if type(_expected) is str:
                return getattr(inspect, 'is{}'.format(expected))(value)

            expected = _expected

        # Check None type
        if expected is None:
            return value is None

        return isinstance(value, expected)
