# -*- coding: utf-8 -*-
import sys
import logging
from colorama import Fore, Style

# Create logger instance for grappa
log = logging.getLogger('grappa')

# Custom log message formatter with colored output
formatter = logging.Formatter(
    u'{}=>{} {}[grappa]{} {}%(asctime)s{} | %(message)s'.format(
        Fore.GREEN,
        Style.RESET_ALL,
        Fore.MAGENTA,
        Style.RESET_ALL,
        Fore.CYAN,
        Style.RESET_ALL,
    )
)

# Create log handler with custom text formatter
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
log.addHandler(handler)

# Set default logging level
log.setLevel(logging.CRITICAL)
