#!/usr/bin/env python3

'''Complex types - functions.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> callable[[float], float]:  # or (int | float)) -> float:
    '''make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.
    '''
    return lambda x: x * multiplier
