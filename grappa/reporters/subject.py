# -*- coding: utf-8 -*-
from ..empty import empty
from .base import BaseReporter
from ..operator_dsl import Message


class SubjectMessageReporter(BaseReporter):

    # Report section title
    title = 'What we got instead'

    # Attribute to lookup in the operator instance for custom message template
    attribute = 'subject'

    def run(self, error):
        if not hasattr(error, 'operator'):
            return None

        # Custom value human-friendly message
        value = self.from_operator(
            self.attribute, getattr(self.ctx, self.attribute, empty)
        )

        # If value empty, return its value accordingly
        if value is empty:
            return None
        if value is None:
            return None if self.attribute == 'expected' else 'None'

        # Get first argument, if needed
        if self.attribute == 'expected' and isinstance(value, (list, tuple)):
            value = value[0] if len(value) == 1 else value

        # Get expectation message, if present in the operator
        attribute = '{}_message'.format(self.attribute)
        text_message = self.from_operator(attribute, None)

        if text_message:
            # Check if message is present and is a negation expression
            if isinstance(text_message, Message):
                attr = 'negation' if self.ctx.negate else 'allowance'
                text_message = getattr(text_message, attr, '')

            # Render template
            text_message = self.render_tmpl(
                self.indentify(text_message),
                self.normalize(value)
            )

        # Return template text message
        return text_message or self.normalize(value)
