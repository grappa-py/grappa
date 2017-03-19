from . import (
    assertion, code, diff, error, expected,
    information, message, reasons, subject
)

# Symbols to export
__all__ = ('reporters',)

# Stores error message reporters
# Reporters will be executed in definition order.
reporters = [
    assertion.AssertionReporter,
    message.MessageReporter,
    error.UnexpectedError,
    reasons.ReasonsReporter,
    expected.ExpectedMessageReporter,
    subject.SubjectMessageReporter,
    information.InformationReporter,
    diff.DiffReporter,
    code.CodeReporter,
]
