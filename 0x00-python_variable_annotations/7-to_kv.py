#!/usr/bin/env python3
"""_summary_
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """_summary_

    Args:
        k (str): _description_
        v (Union[int, float]): _description_

    Returns:
        Tuple[str,float]: _description_
    """
    return (k, v**2)
