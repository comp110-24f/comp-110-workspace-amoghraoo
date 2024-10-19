"""Testing the max function"""

__author__ = 730672928

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max() -> None:
    test_case: list[int] = [5, 6, 11, 7, 1]
    assert find_and_remove_max(test_case) == 11


def test_find_and_remove_max2() -> None:
    test_case: list[int] = [5, 6, 11, 7, 1]
    find_and_remove_max(test_case)
    assert test_case == [5, 6, 7, 1]


def test_find_and_remove_max3() -> None:
    assert find_and_remove_max([]) == -1
