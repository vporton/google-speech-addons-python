#!/usr/bin/env python3

import pytest
from speech_addons.synth_addons import sentences_splitter


class TestSplit:
    def test_dot(self):
        assert sentences_splitter("abc") == ['abc']
        assert sentences_splitter("abc.") == ['abc.']
        assert sentences_splitter("abc", 2) == ['ab', 'c']
        assert sentences_splitter("a. bc", 3) == ['a.', 'bc']
        assert sentences_splitter("a. bc", 2) == ['a.', 'bc']
        assert sentences_splitter("a. bcd", 2) == ['a.', 'bc', 'd']
        assert sentences_splitter("a hj. bc d.", 6) == ['a hj.', 'bc d.']
        assert sentences_splitter("c. ab... d", 7) == ['c.', 'ab... d']
        assert sentences_splitter("c. ab... d", 8) == ['c.', 'ab... d']
