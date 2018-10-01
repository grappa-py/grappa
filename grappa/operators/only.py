import six
from grappa.log import log
from .contain import ContainOperator
from ..operator import Operator


class ContainOnlyOperator(ContainOperator):
    """
    Asserts if only the given value or values can be found
    in a another object.

    Example::

        # Should style
        ['foo', 'bar'] | should.contain.only('foo', 'bar')
        [{'foo': True}, 'bar'] | should.contain.only({'foo': True}, 'bar')

        # Should style - negation form
        ['foo', 'bar'] | should.do_not.contain.only('baz')
        ('foo', 'bar') | should.do_not.contain.only('foo', 'bar', 'extra')

        # Expect style
        ['foo', 'bar'] | expect.to.contain.only('foo', 'bar')
        [{'foo': True}, 'bar'] | expect.to.contain.only('bar', {'foo': True})

        # Expect style - negation form
        ['foo', 'bar'] | expect.to_not.contain.only('bar')
        ['foo', 'bar'] | expect.to_not.contain.only('baz', 'foo')
        ['foo', 'bar'] | expect.to_not.contain.only('bar', 'foo', 'extra')
    """
    operators = ('only', 'just',)
    expected_message = Operator.Dsl.Message(
        'a value that contains only "{value}"',
        'a value that does not contain only "{value}"',
    )

    def match(self, subject, *expected):
        contains_all, reasons = super(ContainOnlyOperator, self)\
            .match(subject, *expected)
        # Add check that no other item is in expected
        if contains_all is True:
            # Handle string case
            if isinstance(subject, six.string_types):
                log.warn('String comparison using "only" is not advised')
                return (subject == expected[0]), []
            return super(ContainOnlyOperator, self).match(expected, *subject)
        return contains_all, reasons
