#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from genderumrevelio.skeleton import fib

__author__ = "Christoffer Berglund"
__copyright__ = "Christoffer Berglund"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
