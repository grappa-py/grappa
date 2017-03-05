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

    # Operator keywords
    operators = ('empty',)

    # Parent operators
    parent = []

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a value that is not "None" and "len(x)" is higher than zero'
    )
    subject_message = Operator.Dsl.Message(
        'an object with type "{type}" which its length '
        'cannot be measured via "len(x)"'
    )

    information = (
        Operator.Dsl.Help(
            Operator.Dsl.Description(
                'An empty object is typically tested via "len(x)"',
                'built-in function. Most built-in types and objects in Python',
                'can be tested that way, such as str, list, generator...',
                'as well as any object that implements "__len__()" method',
                'and returns "0" as length.'
            ),
            Operator.Dsl.Reference(
                'https://docs.python.org/3/library/functions.html#len'
            ),
        ),
    )

    def match(self, subject):
        if subject is None:
            return True

        if subject == 0:
            return True

        try:
            return len(subject) == 0
        except TypeError:
            try:
                next(subject)
            except StopIteration:
                return True
        return False
