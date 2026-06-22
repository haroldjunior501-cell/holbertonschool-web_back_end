#!/usr/bin/env python3
"""Module containing async_comprehension coroutine using async generator."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random floats using an async comprehension."""
    return [i async for i in async_generator()]
