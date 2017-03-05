import inspect
from ..operator import Operator


class PassTestOperator(Operator):
    """
    Asserts if a given function passes the test.

    Example::

        # Should style
        'foo' | should.pass_test(lambda x: len(x) > 2)
        [1, 2, 3] | should.pass_function(lambda x: 2 in x)

        # Should style - negation form
        'foo' | should.do_not.pass_test(lambda x: len(x) > 3)
        [1, 2, 3] | should.do_not.pass_function(lambda x: 5 in x)

        # Expect style
        'foo' | expect.to.pass_test(lambda x: len(x) > 2)
        [1, 2, 3] | expect.to.pass_function(lambda x: 2 in x)

        # Expect style - negation form
        'foo' | expect.to_not.pass_test(lambda x: len(x) > 3)
        [1, 2, 3] | expect.to_not.pass_function(lambda x: 5 in x)
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('pass_test', 'pass_function')

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

    def match(self, subject, fn):
        if not any([inspect.isfunction(fn) or inspect.ismethod(fn)]):
            return False, ['matcher argument must be a function or method']
        return fn(subject)
