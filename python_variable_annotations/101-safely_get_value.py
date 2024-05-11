#!/usr/bin/env python3
''' More involved type annotations
'''
from typing import  Mapping, Any, TypeVar, Union


T = TypeVar('T')
Res = Union[Any, T]
Des = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Des  = None) -> Res:
    '''add type annotations to the function.'''
    if key in dct:
        return dct[key]
    else:
        return default
