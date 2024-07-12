#!/usr/bin/env python3
'''
h
e
y
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' returns a Tuble of (k, v^2) '''
    return lambda n: n * multiplier
