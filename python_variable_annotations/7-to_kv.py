#!/usr/bin/env python3

'''Complex types - string and int/float to tuple.
'''
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:  # or (int | float)) -> float:
    '''Return a tuple of a string and a float.
    '''
    return (k, float( v**2))
