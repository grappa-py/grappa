# -*- coding: utf-8 -*-
import re
import linecache
import traceback
import functools
from colorama import Fore, Style

from ..config import config
from .base import BaseReporter


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

    # Regular expression for invokation based expressions
    PIPE_EXPR = re.compile(r'[\|][\s+]?(should|expect)[\.]')
    FN_CALL_EXPR = re.compile(r'(should|expect)[\s+]?[\(|\.]')

    # Context manager based assertions that does not imply new test calls.
    CONTEXT_EXPR = re.compile(
        r'[\.](not)?[\_]?(have|has|be|to|that|\_is|is\_not|'
        r'satisfy|which|that\_is|which\_is|include)[\_]?(not)?[\.]')

    def match_line(self, line):
        return any([
            CodeReporter.PIPE_EXPR.search(line),
            CodeReporter.FN_CALL_EXPR.search(line),
            CodeReporter.CONTEXT_EXPR.search(line)
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
                    head += Fore.RED + '> ' + Style.RESET_ALL
                else:
                    head += '> '
            else:
                head += '  '

            buf.append(indent + head + code)
            return buf

        code = functools.reduce(render_lines, range(lmin, lmax), [])
        return self.header(trace) + (''.join(code))

    def run(self, error):
        if not config.show_code:
            return None

        trace = self.find_trace()
        return self.render_code(trace) if trace else None
