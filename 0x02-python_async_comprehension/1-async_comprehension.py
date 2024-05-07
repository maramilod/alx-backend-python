#!/usr/bin/env python3
"""
hey in this file
the coroutine will collect 10 random numbers
then return the 10 random numbers
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    The coroutine will collect 10 random number
    then return the 10 random numbers
    """
    f: List[float] = []
    async for i in async_generator():
        f.append(i)
    return f
