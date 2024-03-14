#!/usr/bin/env python3
"""safely_get_value function module"""
from typing import Sequence, Any, Union, Mapping, TypeVar


T = TypeVar('T')
Ret = Union[Any, T]
dft = Union[T, None]

def safely_get_value(dct: Mapping, key: Any, default: dft = None) -> Ret:
    """return a value if the key in dic or default
    """
    if key in dct:
        return dct[key]
    else:
        return default