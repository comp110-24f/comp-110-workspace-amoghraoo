"""List Unit Tests - Exercise 5"""

__author__ = "730672928"


def only_evens(evenlist: list[int]) -> list[int]:
    """Returns the list of even numbers from the input list"""
    outputlist: list[int] = []
    for elem in evenlist:
        if (
            elem % 2 == 0
        ):  # I had inititally forgotten what the MOD function was and had to go back to a previous assignment!
            outputlist.append(elem)
    return outputlist


def sub(sublist: list[int], srtindex: int, endindex: int) -> list[int]:
    """Returns a list of the numbers within a specified range"""
    i1: int = 0
    i2: int = 0
    outputlist: list[int] = []
    if (
        srtindex < 0
    ):  # I wonder if these, in the real world, are added after testing for edge cases
        i1 = 0
    else:
        i1 = srtindex
    if endindex > len(sublist):
        i2 = len(sublist)
    else:
        i2 = endindex
    for elem in range(i1, i2):
        outputlist.append(sublist[elem])
    return outputlist


def add_at_index(
    addlist: list[int], number: int, index: int
) -> (
    None
):  # I was first confused how to approach this and then saw the hint! I realized that I needed another "index" to decrease the length by 1
    """Adds the specified input at the specified index"""
    if index < 0 or index > len(addlist):
        raise IndexError("Index is out of bounds for the input list")
    addlist.append(0)
    idx = len(addlist) - 1
    while idx > index:
        addlist[idx] = addlist[idx - 1]
        idx -= 1
    addlist[index] = number
