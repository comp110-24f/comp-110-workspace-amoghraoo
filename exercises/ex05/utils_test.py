"""Testing utils.py"""

__author__ = "730672928"

from exercises.ex05.utils import only_evens, sub, add_at_index

# only_evens Test


def test_only_evens() -> None:
    """Testing one use case of only_evens"""
    test_case: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert only_evens(test_case) == [2, 4, 6]


def test_only_evens2() -> None:
    """Testing another use case of only_evens"""
    test_case: list[int] = [202, 11, 334, 54, 61, 23]
    assert only_evens(test_case) == [202, 334, 54]


def test_only_evens3() -> (
    None
):  # had to think about what would be the edge case for this one
    """Testing a edge case of only_evens"""
    test_case: list[int] = []
    assert only_evens(test_case) == []


# sub Test


def test_sub() -> None:
    """Testing one use case of sub"""
    test_case: list[int] = [1, 2, 3, 4, 5, 6, 7]
    start: int = 1
    end: int = 5
    assert sub(test_case, start, end) == [2, 3, 4, 5]


def test_sub2() -> None:
    """Testing another use case of sub"""
    test_case: list[int] = [10, 15, 20, 25, 30, 35, 40]
    start: int = 3
    end: int = 4
    assert sub(test_case, start, end) == [
        25
    ]  # I had to remind myself that the end index isn't counted!


def test_sub3() -> None:
    """Testing an edge case of sub"""
    test_case: list[int] = [10, 15, 20, 25, 30, 35, 40]
    start: int = -4  # our edge case!
    end: int = 4
    assert sub(test_case, start, end) == [10, 15, 20, 25]


# add_at_index Test


def test_add_at_index() -> None:
    """Testing a use case of add_at_index"""
    test_case: list[int] = [10, 15, 20, 25, 30, 35, 40]
    num: int = 22
    idx: int = 3
    add_at_index(test_case, num, idx)
    assert test_case == [10, 15, 20, 22, 25, 30, 35, 40]


def test_add_at_index2() -> None:
    """Testing another use case of add_at_index"""
    test_case: list[int] = [3, 6, 9, 15, 18, 21]
    num: int = 12
    idx: int = 3
    add_at_index(test_case, num, idx)
    assert test_case == [3, 6, 9, 12, 15, 18, 21]


import pytest


def test_add_at_index3() -> None:
    """Testing an edge case of add_at_index"""
    test_case: list[int] = [3, 6, 9, 15, 18, 21]
    num: int = 12
    idx: int = 7
    with pytest.raises(IndexError):
        add_at_index(test_case, num, idx) == IndexError
