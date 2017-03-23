# -*- coding: utf-8 -*-
from ..operator import Operator


class IndexOperator(Operator):
    """
    Asserts that a given iterable has an item in a specific index.

    Example::

        # Should style
        [1, 2, 3] | should.have.index(2)
        [1, 2, 3] | should.have.index(1)
        [1, 2, 3] | should.have.index.at(1)
        [1, 2, 3] | should.have.index.present(1)
        [1, 2, 3] | should.have.index.at(1).equal.to(2)
        [1, 2, 3] | should.have.index.at(1) > should.be.equal.to(2)

        # Should style - negation form
        [1, 2, 3] | should.not_have.index(4)
        [1, 2, 3] | should.not_have.index.at(4)
        [1, 2, 3] | should.have.index.at(1).to_not.equal.to(5)

        # Expect style
        [1, 2, 3] | expect.to.have.index(2)
        [1, 2, 3] | expect.to.have.index.at(1)
        [1, 2, 3] | expect.to.have.index.at(1).equal.to(2)
        [1, 2, 3] | expect.to.have.index.at(1) > expect.be.equal.to(2)

        # Expect style - negation form
        [1, 2, 3] | expect.to_not.have.index(2)
        [1, 2, 3] | expect.to_not.have.index.at(1)
        [1, 2, 3] | expect.to_not.have.index.at(1).equal.to(2)
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('index',)

    # Operator chain aliases
    aliases = ('present', 'exists', 'at')

    # Expected message templates
    expected_message = Operator.Dsl.Message(
        'a list/tuple that has index at {value}',
        'a list/tuple that has not index at {value}',
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an object of type "{type}" of length {length} with value "{value}"',
    )

    def match(self, subject, index, **kw):
        if self._not_valid(subject):
            return False, ['subject is not a tuple/list']

        # Get latest item
        if index == -1:
            index = len(subject) - 1

        # Ensure there is a valid index
        if index < 0 or index >= len(subject):
            return False, ['index {0!r} not found'.format(index)]

        # Expose value as subject
        self.ctx.subject = subject[index]

        return True, []

    def _not_valid(self, subject):
        return not isinstance(subject, (list, tuple))
