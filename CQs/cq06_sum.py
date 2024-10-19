"""Summing the elements of a list using different loops"""

__author__ = "730672928"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of elements in a list"""
    idx: int = 0
    sum_vals: float = 0
    if vals == []:
        sum_vals = 0.0
    else:
        while idx < len(vals):
            sum_vals = sum_vals + vals[idx]
            idx += 1
    return sum_vals


def f_sum(vals2: list[float]) -> float:
    """Returns the sum of elements in a list"""
    sum_vals2: float = 0
    if vals2 == []:
        sum_vals2 = 0.0
    else:
        for elem in vals2:
            sum_vals2 = sum_vals2 + elem
    return sum_vals2


def f_range_sum(vals3: list[float]) -> float:
    """Returns the sum of elements in a list"""
    sum_vals3: float = 0
    if vals3 == []:
        sum_vals3 = 0.0
    else:
        for idx in range(0, len(vals3)):
            sum_vals3 = sum_vals3 + vals3[idx]
    return sum_vals3
