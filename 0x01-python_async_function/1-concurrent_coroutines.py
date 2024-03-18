#!/usr/bin/env python3
"""Basic Async"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Wait N"""
    return sorted([await wait_random(max_delay) for _ in range(n)])
