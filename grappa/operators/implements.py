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

    # Operator keywords
    operators = ('implements', 'implement', 'satisfies', 'satisfy')

    # Operaror chain aliases
    aliases = ('interface', 'methods', 'method')

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a value that contains "{value}"',
        'a value that does not contains "{value}"',
    )
    subject_message = Operator.Dsl.Message(
        'an value of type "{type}" with content "{value}"',
    )

    information = (
        Operator.Dsl.Help(
            Operator.Dsl.Description(
                '"None" is a built-in constant in Python that represents the',
                'absence of a value, as when default arguments are not passed',
                'to a function. The sole value of the type NoneType.',
            ),
            Operator.Dsl.Reference(
                'https://docs.python.org/3/library/constants.html#None'
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
