# -*- coding: utf-8 -*-


class GrappaAssertionError(AssertionError):
    """
    GrappaAssertionError represents an internal grappa assertion error
    and it is used internally to encapsulate and share state on
    assertion errors.

    Attributes:
        error (Exception): stores original error exception.
        reasons (list|tuple[str]): stores error reason details.
        operator (Operator): original operator instance that failed.
    """

    def __init__(self, error=None, reasons=None, operator=None):
        self.error = error
        self.reasons = reasons or getattr(error, 'reasons', None)
        self.operator = operator
