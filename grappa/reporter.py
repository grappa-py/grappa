# -*- coding: utf-8 -*-
from .reporters import reporters
from .template import ErrorTemplate


class ErrorReporter(object):
    """
    ErrorReporter renders a given assertion error based on the
    built-in error reporters.
    """

    def __init__(self, ctx):
        self.ctx = ctx

    def render_reporters(self, template, error):
        for Reporter in reporters:
            report = Reporter(self.ctx, error).run(error)
            template.block(Reporter.title, report)

    def run(self, error):
        # Create error template generator
        template = ErrorTemplate()

        # Trigger registered reporters
        try:
            self.render_reporters(template, error)
        except Exception as err:
            err.__legit__ = True
            return err

        # Create assertion error
        err = AssertionError(template.render())

        # Flag error as grappa generated error
        err.__grappa__ = True
        err.error = error
        err.context = self.ctx

        return err
