#!/usr/bin/env python3
"""Element lenfht function module"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''return a list of tuple
    '''
    return [(i, len(i)) for i in lst]
