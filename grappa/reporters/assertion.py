# -*- coding: utf-8 -*-
from ..empty import empty
from .base import BaseReporter


class AssertionReporter(BaseReporter):

    title = 'The following assertion was not satisfied'

    template = 'subject "{}" {} {}'

    def run(self, error):
        # Assertion expression value
        subject = self.normalize(
            self.from_operator('subject', self.ctx.subject), use_raw=False)

        # List of keyword operators DSL
        operators = ' '.join(self.ctx.keywords).replace('_', ' ')

        # Assertion expression value
        assertion = self.template.format(subject, self.ctx.style, operators)

        # Expected value
        expected = self.from_operator('expected', self.ctx.expected)

        if isinstance(expected, tuple):
            if len(expected) == 0:
                expected = empty
            if len(expected) == 1:
                expected = expected[0]

        # Add expected value template, if needed
        if expected is not empty:
            if isinstance(expected, (tuple, list)):
                expected = ', '.join(str(i) for i in expected)
            assertion += ' "{}"'.format(
                self.normalize(expected, use_raw=False))

        return assertion
