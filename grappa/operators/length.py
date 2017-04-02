# -*- coding: utf-8 -*-
from ..operator import Operator


class LengthOperator(Operator):
    """
    Asserts that a given iterable object has exact length.

    Example::

        # Should style
        'foo' | should.have.length(3)
        [1, 2, 3] | should.have.length.of(3)
        iter([1, 2, 3]) | should.have.length.equal.to(3)

        # Should style - negation form
        'foobar' | should.not_have.length(3)
        [1, 2, 3, 4] | should.not_have.length.of(3)
        iter([1, 2, 3, 4]) | should.not_have.length.equal.to(3)

        # Expect style
        'foo' | expect.to.have.length(3)
        [1, 2, 3] | expect.to.have.length.of(3)
        iter([1, 2, 3]) | expect.to.have.length.equal.to(3)

        # Expect style - negation form
        'foobar' | expect.to_not.have.length(3)
        [1, 2, 3, 4] | expect.to_not.have.length.of(3)
        iter([1, 2, 3, 4]) | expect.to_not.have.length.equal.to(3)
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('length', 'size')

    # Operator chain aliases
    aliases = ('equal', 'to', 'of')

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'an object that its length is equal to {value}',
        'an object that its length is not equal to {value}',
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an object of type "{type}" with length {length}'
    )

    information = (
        Operator.Dsl.Help(
            Operator.Dsl.Description(
                'Object length is measured by using "len()" built-in',
                'Python function or consuming an lazy iterable, such as a',
                'generator. Most built-in types and objects in Python',
                'can be tested that way, such as str, list, tuple, dict...',
                'as well as any object that implements "__len__()" method.'
            ),
            Operator.Dsl.Reference(
                'https://docs.python.org/3/library/functions.html#len'
            ),
        ),
    )

    def __init__(self, *args, **kw):
        Operator.__init__(self, *args, **kw)

    def is_number(self, subject):
        return isinstance(subject, (int, float))

    def on_access(self, subject):
        # If already a number, just continue with it
        if self.is_number(subject):
            self.ctx.length = False
            return True, []

        # Set original subject reference
        try:
            self.ctx.subject = len(subject)
            self.ctx.length = False
        except:
            return False, ['cannot measure length of the given object']

        return True, []

    def match(self, subject, expected):
        try:
            length = subject if self.is_number(subject) else len(subject)
            return length == expected, [
                'unexpected object length: {}'.format(length)]
        except TypeError:
            try:
                return len([i for i in subject]) == expected
            except Exception:
                pass
        return False, ['cannot measure the length of the given object']
