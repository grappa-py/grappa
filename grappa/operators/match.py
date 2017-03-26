# -*- coding: utf-8 -*-
import re

from ..operator import Operator


class MatchOperator(Operator):
    """
    Asserts if a given string matches a given regular expression.

    Example::

        # Should style
        'hello world' | should.match(r'Hello \w+')
        'hello world' | should.match(r'hello [A-Z]+', re.I))
        'hello world' | should.match.expression(r'hello [A-Z]+', re.I))

        # Should style - negation form
        'hello w0rld' | should.do_not.match(r'Hello \w+')
        'hello w0rld' | should.do_not.match(r'hello [A-Z]+', re.I))
        'hello world' | should.do_not.match.expression(r'hello [A-Z]+', re.I))

        # Expect style
        'hello world' | expect.to.match(r'Hello \w+')
        'hello world' | expect.to.match(r'hello [A-Z]+', re.I))
        'hello world' | expect.to.match.expression(r'hello [A-Z]+', re.I))

        # Expect style - negation form
        'hello w0rld' | expect.to_not.match(r'Hello \w+')
        'hello w0rld' | expect.to_not.match(r'hello [A-Z]+', re.I))
        'hello world' | expect.to_not.match.expression(r'hello [A-Z]+', re.I))
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('match', 'matches')

    # Operator chain aliases
    aliases = (
        'value', 'string', 'expression', 'token',
        'to', 'regex', 'regexp', 'word', 'phrase'
    )

    # Disable diff report
    show_diff = True

    # Expected template message
    expected_message = Operator.Dsl.Message(
        'a string that matches the expression "{value}"',
        'a string that does not match the expression "{value}"',
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an object of type "{type}" with value "{value}"',
    )

    def match(self, subject, expected, *args):
        if not isinstance(subject, str):
            return False, ['subject must be a string, but got "{}"'.format(
                type(subject))]

        if not isinstance(expected, str):
            return False, [
                'value to match must be a string, but got "{}"'.format(
                    type(expected))
            ]

        return re.search(expected, subject, *args) is not None, []
