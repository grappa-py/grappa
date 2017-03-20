# -*- coding: utf-8 -*-
from .base import BaseReporter


class UnexpectedError(BaseReporter):

    title = 'However, an unexpected exception was raised'

    default_reasons = [
        'The assertion raised an unexpected exception, but it should not.',
        'This behavior might be an bug within the testing library or '
        'in a third-party test operator.'
    ]

    def run(self, error):
        err = getattr(error, 'error', None)
        if not err:
            return None

        # Load error reasons
        error.reasons = getattr(error, 'reasons', self.default_reasons)

        # Normalize error message
        return self.indentify(str(err))
