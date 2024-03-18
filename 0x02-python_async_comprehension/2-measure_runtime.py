#!/usr/bin/env python3
"""Measure runtime"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime"""
    s = time.perf_counter()
    coroutines = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coroutines)
    elapsed = time.perf_counter() - s
    return elapsed
