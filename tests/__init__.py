from __future__ import unicode_literals

import logging
import unittest

import sys


root = logging.getLogger()
root.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s : %(levelname)s : %(name)s : %(message)s')
for stream in (sys.stdout, sys.stderr):
    ch = logging.StreamHandler(stream)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    root.addHandler(ch)


class TestCase(unittest.TestCase):
    pass
