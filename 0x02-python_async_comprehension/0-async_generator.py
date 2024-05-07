#!/usr/bin/env python3
"""
hey
"""
import random
import asyncio
from typing import List


async def async_generator() -> List[float]:
    """
    An asynchronous generator that yields a list of random floats over time.
    """
    li: List[float] = []
    for _ in range(10):
        await asyncio.sleep(1)
        li.append(random.uniform(0, 10))
        yield li[-1]


async def print_yielded_values():
    async for i in async_generator():
        print(i)


if __name__ == "__main__":
    asyncio.run(print_yielded_values())
