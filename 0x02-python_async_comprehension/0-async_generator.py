#!/usr/bin/env python3
"""
The coroutine will loop 10 times,
each time asynchronously wait 1 second,
then yield a random number between 0 and 10.
"""
import random
import asyncio
from typing import List


async def async_generator() -> List[float]:
    """
    An asynchronous generator that yields a list
    of random floats over time.
    """
    li: List[float] = []
    for _ in range(10):
        await asyncio.sleep(1)
        li.append(random.uniform(0, 10))
        yield li[-1]


async def print_yielded_values():
    """
     yield a random number
    """
    async for i in async_generator():
        print(i)
