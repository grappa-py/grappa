# -*- coding: utf-8 -*-
from .empty import empty
from .assertion import AssertionProxy


class OperatorResolver(object):
    """
    Resolves and triggers an operator based on its name identifier.

    This class is highly-coupled to `grappa.Test` and consumes `grappa.Engine`
    and `grappa.Context` in order to trigger operator resolution logic.
    """

    def __init__(self, test):
        self.test = test
        self.ctx = test._ctx
        self.engine = test._engine

    def run_attribute(self, operator):
        operator.run()

    def run_accessor(self, operator):
        # Register assertion function
        def assertion(subject):
            self.ctx.subject = subject
            return operator.run(subject)

        # Add assertion function
        self.engine.add_assertion(assertion)

        # Self-trigger tests if running as global
        if self.ctx.chained:
            self.test._trigger()

        return self.test

    def run_matcher(self, operator):
        # Process assert operators
        def wrapper(*expected, **kw):
            # Register keyword call
            self.engine.add_keyword({'call': expected, 'operator': operator})

            # Retrieve optional custom assertion message
            if 'msg' in kw:
                # Set user-defined message
                self.ctx.message = kw.pop('msg')

            def assertion(subject):
                # Register call subjects
                operator.ctx.subject = subject
                operator.ctx.expected = expected
                return operator.run(subject, *expected, **kw)

            # Register assertion function
            self.test._engine.add_assertion(assertion)

            # Trigger tests on function call if running as chained call
            if self.ctx.chained or self.ctx.subject is not empty:
                return self.test._trigger()

            return self.test

        return AssertionProxy(self, operator, wrapper)

    def resolve(self, name):
        # Check if should stop the call chain
        if self.ctx.stop_chain:
            raise RuntimeError(
                'grappa: test operator "{}" does not allow '
                'chained calls.'.format(self.ctx.stop_chain.operator_name))

        # Find an assertion operator by name
        operator = self.engine.find_operator(name)
        if not operator:
            raise AttributeError(
                '"{}" has no assertion operator called "{}"'.format(
                    self.ctx.style, name
                ))

        # Register attribute access
        self.engine.add_keyword(name)

        # Create operator instance with current context
        operator = operator(context=self.ctx, operator_name=name)

        # Check chainable operator logic is enabled
        if getattr(operator, 'chainable', True) is False:
            self.ctx.stop_chain = operator

        # Reset context sequence
        if self.ctx.reset:
            self.engine.reset_keywords()
            self.ctx.reset = False
            # self.ctx.reverse = True

        # Dynamically retrieve operator
        method_name = 'run_{}'.format(operator.kind)
        run_operator = getattr(self, method_name, None)

        # If operator kind is not support, raise an exception
        if not run_operator:
            raise ValueError('operator "{}" has not a valid kind "{}"'.format(
                operator.__class__.__name__,
                operator.kind
            ))

        # Register operator assertion for lazy execution
        return run_operator(operator) or self.test
