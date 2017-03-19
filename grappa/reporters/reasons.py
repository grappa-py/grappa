# -*- coding: utf-8 -*-
from .base import BaseReporter


class ReasonsReporter(BaseReporter):

    title = 'Reasons'

    def run(self, error):
        return getattr(error, 'reasons', None)
