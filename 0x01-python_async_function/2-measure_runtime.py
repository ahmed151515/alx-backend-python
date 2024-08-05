#!/usr/bin/env python3
"""_summary_
    """
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """_summary_

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        float: _description_
    """
    start = time.time()
    wait_n(n, max_delay)
    res = time.time() - start
    return res / n
