#!/usr/bin/python
# coding: utf8

import sys;
from tests.common import test_length, test_comments;

## TODO
# Usage ...
# Flags:
# -o: output
# -h: no header

FLAG_COLOR = 0x1;
FLAG_FULL = 0x2;

flags = 0;

for arg in sys.argv[1:]:
    if arg[0] == '-':
        if 'c' in arg:
            flags |= FLAG_COLOR;
        if 'f' in arg:
            flags |= FLAG_FULL;

test_length();
test_comments();
