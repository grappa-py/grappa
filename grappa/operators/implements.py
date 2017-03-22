# -*- coding: utf-8 -*-
import inspect
import functools
from ..operator import Operator


class ImplementsOperator(Operator):
    """
    Asserts if a given object implements an interface of methods.

    Example::

        class Foo(object):
            def bar():
                pass

            def baz():
                pass

        # Should style
        Foo() | should.implements('bar')
        Foo() | should.implements.method('bar')
        Foo() | should.implement.methods('bar', 'baz')
        Foo() | should.implement.interface('bar', 'baz')
        Foo() | should.satisfies.interface('bar', 'baz')

        # Should style - negation form
        Foo() | should.do_not.implements('bar')
        Foo() | should.do_not.implement.methods('bar', 'baz')
        Foo() | should.do_not.implement.interface('bar', 'baz')
        Foo() | should.do_not.satisfy.interface('bar', 'baz')

        # Expect style
        Foo() | expect.to.implement('bar')
        Foo() | expect.to.implement.method('bar')
        Foo() | expect.to.implement.methods('bar', 'baz')
        Foo() | expect.to.implement.interface('bar', 'baz')
        Foo() | expect.to.satisfy.interface('bar', 'baz')

        # Expect style - negation form
        Foo() | expect.to_not.implement('bar')
        Foo() | expect.to_not.implement.method('bar')
        Foo() | expect.to_not.implement.methods('bar', 'baz')
        Foo() | expect.to_not.implement.interface('bar', 'baz')
        Foo() | expect.to_not.satisfy.interface('bar', 'baz')
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('implements', 'implement', 'interface')

    # Operator chain aliases
    aliases = ('interface', 'methods', 'method')

    # Expected template message
    expected_message = Operator.Dsl.Message(
        'an object that implements the following members "{value}"',
        'an object that does not implement the following members "{value}"',
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an object of type "{type}" with content "{value}"',
    )

    # Assertion information
    information = (
        Operator.Dsl.Help(
            Operator.Dsl.Description(
                'Object interface implementation is verified by using the',
                'Python built-in function "hasattr" along with',
                '"inspect.ismethod()" function in order to infer if a given',
                'object implements the required methods.'
            ),
            Operator.Dsl.Reference(
                'https://docs.python.org/3.6/library/functions.html#hasattr'
            ),
        ),
    )

    def has_method(self, cls, method):
        return any([inspect.ismethod(getattr(cls, method)),
                    inspect.isfunction(getattr(cls, method))])

    def match(self, cls, *methods):
        if len(methods) == 0:
            return False, ['methods to implement cannot be empty']

        def validate(reasons, method):
            if not hasattr(cls, method):
                reasons.append('object does not have property "{}"'.format(
                    method
                ))
            elif not self.has_method(cls, method):
                reasons.append('object does not implement method "{}"'.format(
                    method
                ))
            return reasons

        reasons = functools.reduce(validate, methods, [])
        return len(reasons) == 0, reasons
