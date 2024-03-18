#!/usr/bin/env python3
"""Async Comprehension"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List:
    """Async Comprehension"""
    return [i async for i in async_generator()]
