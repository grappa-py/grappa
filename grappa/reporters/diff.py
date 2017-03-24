# -*- coding: utf-8 -*-
import os
import difflib

from .base import BaseReporter


class DiffReporter(BaseReporter):
    """
    Outputs the comparison differences result between the
    subject/expected objects.
    """

    title = 'Difference comparison'

    def run(self, error):
        # Ensure operator enables diff reporter, otherwise just exit
        show_diff = any([
            self.ctx.show_diff,
            self.from_operator('show_diff', False)
        ])
        if not show_diff:
            return

        # Match if the given operator implements a custom differ
        differ = self.from_operator('differ', None)
        if differ:
            return error.operator.differ()

        # Obtain subject value
        subject = str(
            self.from_operator(
                'diff_subject',
                self.from_operator('subject', self.ctx.subject)))

        # Split subject by lines
        subject = subject.splitlines(1)

        # Obtain expected value
        expected = self.from_operator(
                    'diff_expected',
                    self.from_operator('expected', self.ctx.expected))

        # Get expected value, if needed
        if isinstance(expected, tuple) and len(expected) == 1:
            expected = expected[0]

        # Expected value
        expected = str(expected).splitlines(1)

        # Diff subject and expected values
        data = list(difflib.ndiff(subject, expected))

        # Remove trailing line feed returned by ndiff, if present
        data[-1] = data[-1].replace(os.linesep, '')

        # Normalize line separator with proper indent level
        data = [i.replace(os.linesep, '') for i in data]

        return data
