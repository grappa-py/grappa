# -*- coding: utf-8 -*-
import numbers
from ..operator import Operator


class EmptyOperator(Operator):
    """
    Asserts if a given subject is an empty object.

    A subject is considered empty if it's ``None``, ``0`` or ``len(subject)``
    is equals to ``0``.

    Example::

        # Should style
        [] | should.be.empty

        # Should style - negation form
        [1, 2, 3] | should.not_be.empty

        # Expect style
        tuple() | expect.to.be.empty

        # Expect style - negation form
        (1, 2, 3) | expect.to_not.be.empty
    """

    # Is the operator a keyword
    kind = Operator.Type.ACCESSOR

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('empty',)

    # Expected template message
    expected_message = Operator.Dsl.Message(
        'a value that is not "None" and its length is higher than zero'
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an object with type "{type}" which its length cannot be measured'
    )

    # Assertion information
    information = (
        Operator.Dsl.Help(
            Operator.Dsl.Description(
                'An empty object can be "None", "0" or "len(x) == 0".',
                'Most objects in Python can be tested via "len(x)"',
                'such as str, list, tuple, dict, generator...',
                'as well as any object that implements "__len__()" method.',
            ),
            Operator.Dsl.Reference(
                'https://docs.python.org/3/library/functions.html#len'
            ),
        ),
    )

    def match(self, subject):
        if subject is None or subject is 0:
            return True

        if subject in (True, False):
            return False

        if isinstance(subject, numbers.Number) and subject != 0:
            return False

        try:
            return len(subject) == 0
        except TypeError:
            try:
                next(subject)
            except StopIteration:
                return True
            except Exception:
                return True
        return False
