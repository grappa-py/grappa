# -*- coding: utf-8 -*-
import sys

# True if running Python 2.x
IS_PY2 = sys.version_info[0] == 2

# String types per Python version
STR_TYPES = (str, unicode) if IS_PY2 else (bytes, str)  # noqa
