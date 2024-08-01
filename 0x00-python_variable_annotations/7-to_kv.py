#!/usr/bin/env python3
"""_summary_
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str,float]:
    """_summary_

    Args:
        k (str): _description_
        v (Union[int, float]): _description_

    Returns:
        tuple: _description_
    """
    return (k, v)


print(to_kv.__annotations__)
print(to_kv("eggs", 3))
print(to_kv("school", 0.02))
