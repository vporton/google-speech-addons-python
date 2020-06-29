#!/usr/bin/env python3

import pytest
from synth_addons import mysplit


class TestSplit:
    def test_dot(self):
        assert mysplit("abc") == ['abc']
        assert mysplit("abc.") == ['abc.']
        assert mysplit("abc", 2) == ['ab', 'c']
        assert mysplit("a. bc", 3) == ['a.', 'bc']
        assert mysplit("a. bc", 2) == ['a.', 'bc']
        assert mysplit("a. bcd", 2) == ['a.', 'bc', 'd']
        assert mysplit("a hj. bc d.", 6) == ['a hj.', 'bc d.']
        assert mysplit("c. ab... d", 7) == ['c.', 'ab... d']
        assert mysplit("c. ab... d", 8) == ['c.', 'ab... d']
