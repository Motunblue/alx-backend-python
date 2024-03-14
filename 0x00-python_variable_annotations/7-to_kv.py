#!/usr/bin/env python3
"""to_kv function module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Return the sum of a list
    """
    return (k, v * v)
