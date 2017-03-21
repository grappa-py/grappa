# -*- coding: utf-8 -*-
from ..empty import empty
from .base import BaseReporter


class AssertionReporter(BaseReporter):

    title = 'The following assertion was not satisfied'

    template = 'subject "{}" {} {}'

    def get_expected(self, operator=None, defaults=None):
        # Expected value
        expected = self.from_operator('expected', defaults, operator=operator)

        if isinstance(expected, tuple):
            if len(expected) == 0:
                expected = empty
            if len(expected) == 1:
                expected = expected[0]

        # Add expected value template, if needed
        if expected is not empty:
            if isinstance(expected, (tuple, list)):
                expected = ', '.join(str(i) for i in expected)

            if isinstance(expected, (int, float)):
                return '{}'.format(expected)

            return '"{}"'.format(self.normalize(expected, use_raw=False))

    def run(self, error):
        # Assertion expression value
        subject = self.normalize(
            self.from_operator('subject', self.ctx.subject), use_raw=False)

        # List of used keyword operators
        keywords = []
        for keyword in self.ctx.keywords:
            if type(keyword) is dict and 'operator' in keyword:
                expected = self.get_expected(
                    keyword['operator'], keyword['call'])
                keywords.append(expected or '"Empty"')
            else:
                keywords.append(keyword)

        # Compose assertion sentence
        operators = ' '.join(keywords).replace('_', ' ')

        # Assertion expression value
        assertion = self.template.format(subject, self.ctx.style, operators)

        # Return assertion formatted sentence
        return assertion
