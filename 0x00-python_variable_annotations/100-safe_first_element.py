#!/usr/bin/env python3
"""safe_first_element function module"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return lst[0] or none
    """
    if lst:
        return lst[0]
    else:
        return None
