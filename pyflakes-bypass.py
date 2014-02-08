#!/usr/bin/env python

from pyflakes.scripts import pyflakes
from pyflakes.checker import Checker


def report_with_bypass(self, messageClass, *args, **kwargs):
    if isinstance(args[0], int):
        text_lineno = args[0] - 1
        with open(self.filename, 'r') as code:
            if code.readlines()[text_lineno].find('bypass_pyflakes') >= 0:
                return
    self.messages.append(messageClass(self.filename, *args, **kwargs))

# monkey patch checker to support bypass
Checker.report = report_with_bypass

pyflakes.main()
