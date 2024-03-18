#!/usr/bin/env python3
"""Basic Async"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """Wait N"""
    return [await wait_random(max_delay) for _ in range(n)]
