#!/usr/bin/env python3
"""_summary_
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """_summary_

    Args:
        multiplier (float): _description_

    Returns:
        Callable[[float], float]: _description_
    """
    def multiplies(n: float):
        """_summary_

        Args:
            n (float): _description_

        Returns:
            _type_: _description_
        """        """
        multiply two number
        """
        return n * multiplier
    return multiplies
