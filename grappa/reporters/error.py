# -*- coding: utf-8 -*-
from .base import BaseReporter


class UnexpectedError(BaseReporter):

    title = 'However, an unexpected exception was raised'

    def run(self, error):
        err = getattr(error, 'error', None)
        if not err:
            return None

        error.reasons = [
            'the assertion raised an unexpected exception, but it should not',
            'this behavior might be an bug within the testing library or '
            'in third-party test operators'
        ]

        return str(err)
