#!/usr/bin/env python3
"""
The coroutine will loop 10 times,
each time asynchronously wait 1 second,
then yield a random number between 0 and 10.
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields a list
    of random floats over time.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0, 10))


async def print_yielded_values():
    """
     Print the yielded random numbers.
    """
    async for i in async_generator():
        print(i)
