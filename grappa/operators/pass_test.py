# -*- coding: utf-8 -*-
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

    # Expected message template
    expected_message = Operator.Dsl.Message(
        'a value that passes the test function',
        'a value that does not pass the test function',
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an value of type "{type}" with value "{value}"',
    )

    def match(self, subject, fn):
        if not any([inspect.isfunction(fn) or inspect.ismethod(fn)]):
            return False, ['matcher argument must be a function or method']
        return fn(subject)
