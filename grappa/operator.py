# -*- coding: utf-8 -*-
import inspect
import functools

from .log import log
from .empty import empty
from . import operator_dsl as OperatorDsl
from .exceptions import GrappaAssertionError


class OperatorTypes(object):
    """
    OperatorTypes is used as struct to store the operator types flags.
    """
    # Attribute operators have no validation logic and only defines chained
    # API DSL keywords, typically for test declaration purposes.
    ATTRIBUTE = 'attribute'

    # Accessor operators do not accept expectation arguments and only does
    # static validation logic. E.g: `true/false` operators.
    ACCESSOR = 'accessor'

    # Matcher operators accepts expectation arguments and does the validation
    # based on them. E.g: `equal`.
    MATCHER = 'matcher'


class Operator(object):
    """
    Operator implements a base class with common logic and required interface
    that is used by specific operator implementations.

    Any operator should inherit from this class.

    Attributes:
        Dsl (grappa.operators_dsl): DSL for operator error messages templating
        Type (grappa.operators.OperatorTypes): support operators types
        kind (str): stores the operator kind
        operators (list|tuple): operator keywords
        aliases (list|tuple): chain attributes aliases for expressivity
        information (list|tuple): optional additional help in case of error
        subject_message (str|Operator.Dsl.Message): optional subject message
        expected_message (str|Operator.Dsl.Message): optional expected message
        operator_name (str): invokation operator name keyword
        suboperators (list|tuple[grappa.Operator]): optional child operators
    """

    # Shortcut alias for operator DSL module
    Dsl = OperatorDsl

    # Shortcut to the supported operator types
    Type = OperatorTypes

    # Stores operator kind
    kind = OperatorTypes.MATCHER

    # Operator keywords
    operators = tuple()

    # Chain alias keywords
    aliases = tuple()

    # Enable/disable operator chaining
    chainable = True

    # Stores assertion error tips
    information = []

    # Stores test execution context
    ctx = None

    # Stores the selected operator name when executed
    operator_name = None

    # Stores optional suboperators (not supported yet)
    suboperators = []

    # Stores optionally yielded operator result value
    value = empty

    # Stores operator assertion expectation
    expected = empty

    # Default subject error template
    subject_message = Dsl.Message(
        'a value of "{type}" type with content "{value}"'
        'a value of "{type}" type with content "{value}"'
    )

    # Default expected error template
    expected_message = Dsl.Message(
        'a value of "{type}" type that satisfies assertion with "{value}"',
        'a value of "{type}" type that does not satisfies assertion '
        'with "{value}"',
    )

    def __init__(self, context=None, operator_name=None, fn=None,
                 kind=None, aliases=None, operators=None, suboperators=None):
        if inspect.isfunction(fn):
            self.match = fn
        if kind:
            self.kind = kind
        if operators:
            self.operators = operators
        if aliases:
            self.aliases = aliases
        if context:
            self.ctx = context
        if operator_name:
            self.operator_name = operator_name
        if suboperators:
            self.suboperators = suboperators

    def match(self, *args, **kw):
        raise NotImplementedError('"match" method must be implemented')

    def __call__(self, *args, **kw):
        """
        Overloads function invokation in current operator and creates a new
        cloned operator instance.
        """
        operator = Operator()
        operator.__dict__ = self.__dict__.copy()
        operator.__init__(*args, **kw)
        return operator

    def observe(matcher):
        """
        Internal decorator to trigger operator hooks before/after
        matcher execution.
        """
        @functools.wraps(matcher)
        def observer(self, subject, *expected, **kw):
            # Trigger before hook, if present
            if hasattr(self, 'before'):
                self.before(subject, *expected, **kw)

            # Trigger matcher method
            result = matcher(self, subject, *expected, **kw)

            # After error hook
            if result is not True and hasattr(self, 'after_error'):
                self.after_error(result, subject, *expected, **kw)

            # After success hook
            if result is True and hasattr(self, 'after_success'):
                self.after_success(subject, *expected, **kw)

            # Enable diff comparison on error, if needed
            if not hasattr(self, 'show_diff'):
                self.show_diff = all([
                    isinstance(subject, str),
                    all([isinstance(x, str) for x in expected]),
                ])

            return result
        return observer

    def _make_error(self, reasons=None, error=None):
        return GrappaAssertionError(
            error=error,
            reasons=reasons,
            operator=self
        )

    @observe
    def run_matcher(self, subject, *expected, **kw):
        """
        Runs the operator matcher test function.
        """
        # Update assertion expectation
        self.expected = expected

        _args = (subject,)
        if self.kind == OperatorTypes.MATCHER:
            _args += expected

        try:
            result = self.match(*_args, **kw)
        except Exception as error:
            return self._make_error(error=error)

        reasons = []
        if isinstance(result, tuple):
            result, reasons = result

        if result is False and self.ctx.negate:
            return True

        if result is True and not self.ctx.negate:
            return True

        return self._make_error(reasons=reasons)

    def run(self, *args, **kw):
        """
        Runs the current operator with the subject arguments to test.

        This method is implemented by matchers only.
        """
        log.debug('[operator] run "{}" with arguments: {}'.format(
            self.__class__.__name__, args
        ))

        if self.kind == OperatorTypes.ATTRIBUTE:
            return self.match(self.ctx)
        else:
            return self.run_matcher(*args, **kw)

    def __enter__(self):
        raise NotImplementedError('operator cannot be used as "with" statement')  # noqa

    def __exit__(self, etype, value, traceback):
        self.__enter__()
