#!/usr/bin/env python3
"""_summary_

    Yields:
        _type_: _description_
    """
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """_summary_

    Returns:
        AsyncGenerator[float, None]: _description_

    Yields:
        Iterator[AsyncGenerator[float, None]]: _description_
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
