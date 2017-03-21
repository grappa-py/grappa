# -*- coding: utf-8 -*-
from .reporter import ErrorReporter


class Runner(object):
    """
    Runner is responsible of triggering the registed assertion operators in the
    current engine.

    Arguments:
        engine (grappa.Engine)
    """

    def __init__(self, engine):
        self.engine = engine

    def render_error(self, ctx, error):
        # Expose keywords via context (this should be improved)
        ctx.keywords = self.engine.keywords
        # Render error exception
        return ErrorReporter(ctx).run(error)

    def run_assertions(self, ctx):
        # Trigger assertion functions
        for assertion in self.engine.assertions:
            # Store current subject
            subject = ctx.subject

            # Run assertion with the given subject
            result = assertion(ctx.subject)

            # Check if the subject changed during operator execution
            if subject is not ctx.subject:
                # Register previous subject
                ctx.subjects.append(subject)

            # If assertion passed, just continue with it
            if result is True:
                continue

            # Forward original grappa error
            if all([isinstance(result, AssertionError),
                    hasattr(result, '__grappa__')]):
                return result

            # Otherwise render assertion error accordingly
            return self.render_error(ctx, result)

    def run(self, ctx):
        """
        Runs the current phase.
        """
        # Reverse engine assertion if needed
        if ctx.reverse:
            self.engine.reverse()

        if self.engine.empty:
            raise AssertionError('grappa: no assertions to run')

        try:
            # Run assertion in series and return error, if present
            return self.run_assertions(ctx)
        except Exception as _err:
            # Handle legit grappa internval errors
            if getattr(_err, '__legit__', False):
                raise _err
            # Otherwise render it
            return self.render_error(ctx, _err)
