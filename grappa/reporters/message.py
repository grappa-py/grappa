# -*- coding: utf-8 -*-
from .base import BaseReporter


class MessageReporter(BaseReporter):

    title = 'Message'

    def run(self, error):
        return self.ctx.message
