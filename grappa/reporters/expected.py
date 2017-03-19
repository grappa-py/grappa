# -*- coding: utf-8 -*-
from .subject import SubjectMessageReporter


class ExpectedMessageReporter(SubjectMessageReporter):

    title = 'What we expected'

    # Attribute to lookup in the operator instance for custom message template
    attribute = 'expected'
