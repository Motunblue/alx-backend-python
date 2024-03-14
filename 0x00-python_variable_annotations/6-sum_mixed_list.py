#!/usr/bin/env python3
"""sum_mixed_list function module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Return the sum of a list

        Args:
            input_list (List): list of float and int
    """
    return sum(mxd_lst)
