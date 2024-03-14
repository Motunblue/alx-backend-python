#!/usr/bin/env python3
"""make_multiplier function module"""
from typing import Callable


def make_multiplier(multiplier: float) ->Callable [[float], float]:
    """ Return the sum of a list
    """
    return lambda x: x * multiplier
