#!/usr/bin/env python3
"""Module for measuring the runtime of the wait_n coroutine."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure total execution time for wait_n and return time per coroutine."""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start
    return total_time / n
