# -*- coding: utf-8 -*-
import re
import os
import difflib
import linecache
import traceback
import functools
from colorama import Fore, Style

from .empty import empty
from .config import config
from .operator_dsl import Message
from .template import ErrorTemplate


class BaseReporter(object):

    def __init__(self, ctx, error):
        self.ctx = ctx
        self.error = error

    def cut(self, value, size=50):
        text = str(value)
        return text[0:size] + ' ...' if len(text) > size else text

    def linefy(self, value):
        return str(value).replace(os.linesep, r'\n')

    def normalize(self, value, size=20):
        if value is None:
            return value

        try:
            value = str(value)
        except:
            value = value

        if not hasattr(value, '__len__'):
            return value

        return self.linefy(self.cut(value))

    def safe_length(self, value):
        try:
            return len(value)
        except:
            return '"unmeasurable"'

    def from_operator(self, name, defaults=None):
        if not hasattr(self.error, 'operator'):
            return defaults
        value = getattr(self.error.operator, name, defaults)
        return defaults if value is empty else value

    def render_tmpl(self, tmpl, value):
        placeholders = {}

        if '{value}' in tmpl:
            placeholders['value'] = self.normalize(value)

        if '{type}' in tmpl:
            placeholders['type'] = type(value).__name__

        if '{length}' in tmpl:
            placeholders['length'] = self.safe_length(value)

        return tmpl.format(**placeholders)

    def run(self, error):
        raise NotImplementedError('run() method must be implemented')


class AssertionReporter(BaseReporter):

    title = 'The following assertion was not satisfied'

    template = 'subject "{}" {} {}'

    def run(self, error):
        # Assertion expression value
        subject = self.normalize(
            self.from_operator('subject', self.ctx.subject))

        # List of keyword operators DSL
        operators = ' '.join(self.ctx.keywords).replace('_', ' ')

        # Assertion expression value
        assertion = self.template.format(subject, self.ctx.style, operators)

        # Expected value
        expected = self.from_operator('expected', self.ctx.expected)

        if isinstance(expected, tuple):
            if len(expected) == 0:
                expected = empty
            if len(expected) == 1:
                expected = expected[0]

        # Add expected value template, if needed
        if expected is not empty:
            if isinstance(expected, (tuple, list)):
                expected = ', '.join(str(i) for i in expected)
            assertion += ' "{}"'.format(self.normalize(expected))

        return assertion


class SubjectMessageReporter(BaseReporter):

    title = 'What we got instead'

    # Attribute to lookup in the operator instance for custom message template
    attribute = 'subject'

    def run(self, error):
        if not hasattr(error, 'operator'):
            return None

        # Custom value human-friendly message
        value = self.from_operator(self.attribute,
                                   getattr(self.ctx, self.attribute, empty))

        if value is empty:
            return None

        if value is None:
            return None if self.attribute == 'expected' else 'None'

        # Get first argument, if needed
        if self.attribute == 'expected' and len(value) == 1:
            value = value[0]

        # Get expectation message, if present in the operator
        attribute = '{}_message'.format(self.attribute)
        text_message = self.from_operator(attribute, None)
        if text_message:
            if isinstance(text_message, Message):
                attr = 'negation' if self.ctx.negate else 'allowance'
                text_message = getattr(text_message, attr, '')

            # Render template
            text_message = self.render_tmpl(text_message, value)

        return text_message or self.normalize(value)


class ExpectedMessageReporter(SubjectMessageReporter):

    title = 'What we expected'

    # Attribute to lookup in the operator instance for custom message template
    attribute = 'expected'


class MessageReporter(BaseReporter):

    title = 'Message'

    def run(self, error):
        return self.ctx.message


class ErrorReasonsReporter(BaseReporter):

    title = 'Reasons'

    def run(self, error):
        return getattr(error, 'reasons', None)


class InformationReporter(BaseReporter):

    title = 'Information'

    def run(self, error):
        return self.from_operator('information', None)


class UnexpectedError(BaseReporter):

    title = 'However, an unexpected exception was raised'

    def run(self, error):
        err = getattr(error, 'error', None)
        if not err:
            return None

        error.reasons = [
            'the assertion raised an unexpected exception, but it should not',
            'this behavior might be an bug within the testing library or '
            'in third-party test operators'
        ]

        return str(err)


class Trace(object):
    """
    Python < 3.4 traceback compatibility wrapper for Python +3.5
    """

    def __init__(self, trace):
        self.name = trace[2]
        self.line = trace[-1]
        self.lineno = trace[1]
        self.filename = trace[0]


class CodeReporter(BaseReporter):
    """
    CodeReporter matches and renders the fragment of the code
    """

    title = 'Where'

    LINES = 8
    INDENT_SPACES = 4

    PIPE_EXPR = re.compile(r'[\|][\s+]?(should|expect)[\.]')
    FN_CALL_EXPR = re.compile(r'(should|expect)[\s+]?[\(|\.]')

    def match_line(self, line):
        return any([
            CodeReporter.PIPE_EXPR.search(line),
            CodeReporter.FN_CALL_EXPR.match(line),
        ])

    def find_trace(self):
        # Get latest exception stack
        trace_list = list(traceback.extract_stack())
        trace_list.reverse()

        for trace in trace_list:
            # Normalize traceback in old Python versions
            if isinstance(trace, tuple):
                trace = Trace(trace)
            # Match code line
            if self.match_line(trace.line):
                return trace

    def header(self, trace):
        return 'File "{}", line {}, in {}\n\n'.format(
            trace.filename,
            trace.lineno,
            trace.name,
        )

    def render_code(self, trace):
        lmin = trace.lineno - CodeReporter.LINES
        lmax = trace.lineno + CodeReporter.LINES
        max_len = max(len(str(lmin)), len(str(lmax)))

        def calculate_space(line):
            return ' ' * (max_len - len(str(line)))

        def render_lines(buf, line):
            # Retrieve line of code from the trackback
            code = linecache.getline(trace.filename, line)
            if len(code) == 0:
                return buf

            # Calculate indentation and line head space for aligment
            space = calculate_space(line)
            indent = ' ' * CodeReporter.INDENT_SPACES

            # Line head
            head = '{}{}{}| {}'.format(
                Fore.GREEN if config.use_colors else '',
                space, line,
                Style.RESET_ALL if config.use_colors else ''
            )

            if line == trace.lineno:
                if config.use_colors:
                    head += Fore.RED + '>' + Style.RESET_ALL
                else:
                    head += '>'
            else:
                head += ' '

            buf.append(indent + head + code)
            return buf

        code = functools.reduce(render_lines, range(lmin, lmax), [])
        return self.header(trace) + (''.join(code))

    def run(self, error):
        if not config.show_code:
            return None

        trace = self.find_trace()
        return self.render_code(trace) if trace else None


class DiffReporter(BaseReporter):
    """
    Outputs the comparison differences result between the
    subject/expected objects.
    """

    title = 'Difference comparison'

    def run(self, error):
        # Ensure operator enables diff reporter, otherwise just exit
        show_diff = any([
            self.ctx.show_diff,
            self.from_operator('show_diff', False)
        ])
        if not show_diff:
            return

        # Match if the given operator implements a custom differ
        differ = self.from_operator('differ', None)
        if differ:
            return error.operator.differ()

        # Obtain subject/expected values
        subject = str(self.from_operator('subject', self.ctx.subject))
        expected = str(self.from_operator('expected', self.ctx.expected))

        # Expected results
        if isinstance(expected, tuple) and len(expected) == 1:
            expected = expected[0]

        # Diff subject and expected values
        data = list(difflib.ndiff([subject], [expected]))

        # Remove trailing line feed
        data[-1] = data[-1].replace(os.linesep, '')

        return data


class ErrorReporter(object):
    """
    ErrorReporter renders the current error code.
    """

    # Stores error message reporters
    # Reporters will be executed in definition order.
    REPORTERS = [
        AssertionReporter,
        MessageReporter,
        UnexpectedError,
        ErrorReasonsReporter,
        ExpectedMessageReporter,
        SubjectMessageReporter,
        InformationReporter,
        DiffReporter,
        CodeReporter,
    ]

    def __init__(self, ctx):
        self.ctx = ctx

    def render_reporters(self, template, error):
        for Reporter in ErrorReporter.REPORTERS:
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
