#!/usr/bin/env python3

from src.__main__ import add

def test_add():
    assert add(1, 2) == 3, "Math failed"
