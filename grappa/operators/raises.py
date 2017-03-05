import inspect
from ..operator import Operator


class RaisesOperator(Operator):
    """
    Asserts if a given function raises an exception.

    Example::

        def fn():
            raise ValueError('error')

        # Should style
        fn | should.raise_error()
        fn | should.raise_error(ValueError)
        fn | should.raise_error(AttributeError, ValueError)

        # Should style - negation form
        fn | should.do_not.raise_error()
        fn | should.do_not.raise_error(ValueError)
        fn | should.do_not.raise_error(AttributeError, ValueError)

        # Expect style
        fn | expect.to.raise_error()
        fn | expect.to.raise_error(ValueError)
        fn | expect.to.raise_error(AttributeError, ValueError)

        # Expect style - negation form
        fn | expect.to_not.raise_error()
        fn | expect.to_not.raise_error(ValueError)
        fn | expect.to_not.raise_error(AttributeError, ValueError)
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('raises', 'raise_error', 'raise_errors')

    # Operaror chain aliases
    aliases = ('to', 'that', 'are', 'instance', 'of')

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a value that contains "{value}"',
        'a value that does not contains "{value}"',
    )
    subject_message = Operator.Dsl.Message(
        'an value of type "{type}" with content "{value}"',
    )

    information = (
        Operator.Dsl.Help(
            Operator.Dsl.Description(
                '"None" is a built-in constant in Python that represents the',
                'absence of a value, as when default arguments are not passed',
                'to a function. The sole value of the type NoneType.',
            ),
            Operator.Dsl.Reference(
                'https://docs.python.org/3/library/constants.html#None'
            ),
        ),
    )

    def match(self, fn, *errors):
        if not any([inspect.isfunction(fn) or inspect.ismethod(fn)]):
            return False, ['subject must be a function or method']

        try:
            fn()
        except Exception as err:
            self.value = err

            # If no errors present, just raise the exception
            if not errors:
                return True, []

            # Otherwise match errors
            return isinstance(err, *errors), ['invalid raised exception']
        else:
            return False, ['did not raise any exception']
