# -*- coding: utf-8 -*-
from colorama import Fore, Style


class Message(object):

    def __init__(self, allowance=None, negation=None):
        self.allowance = allowance
        self.negation = negation or allowance

    def render(self, negation=False):
        return self.negation if negation else self.allowance


class Description(object):

    ARROW = '>'

    def __init__(self, *text):
        self.value = text

    def render(self, separator):
        lines = '\n{}'.format(separator).join(self.value)
        return Description.ARROW + ' ' + lines


class Reference(object):

    TOKEN = '=>'
    TEXT = 'Reference'

    def __init__(self, url=None):
        self.url = url

    def render(self, separator):
        return separator + '{}{}{} {}{}: {}{}'.format(
            Fore.CYAN,
            Reference.TOKEN,
            Style.RESET_ALL,
            Fore.GREEN,
            Reference.TEXT,
            self.url,
            Style.RESET_ALL,
        )


class Help(object):

    def __init__(self, description=None, *references):
        self.description = description
        self.references = references

    def render(self, separator):
        description = self.description.render(separator)
        references = [ref.render(separator) for ref in self.references]
        return '\n'.join([description] + references)
