# -*- coding: utf-8 -*-
from .base import BaseReporter


class InformationReporter(BaseReporter):

    title = 'Information'

    def run(self, error):
        return self.from_operator('information', None)
