"""List Utility Functions in Python!"""

__author__ = "730672928"


def all(list1: list[int], var1: int) -> bool:
    """If a int matches all the values in a list, return T or F"""
    condition: bool = False
    for (
        elem
    ) in (
        list1
    ):  # thought about using a while loop at first but realized that a for loop works better!
        if elem == var1:
            condition = True
        else:
            return False
    return condition


def max(maxlist: list[int]) -> int:
    """Return the max value of a list"""
    if (
        len(maxlist) == 0
    ):  # first had this statement after defining the compare variable, found out that it encounters an error before that
        raise ValueError("max() arg is an empty List")
    compare: int = maxlist[0]
    idx: int = 0
    while idx < len(maxlist):
        if maxlist[idx] > compare:
            compare = maxlist[idx]
        idx += 1
    idx = 0
    return compare


def is_equal(lista: list[int], listb: list[int]) -> bool:
    """Checks if two lists are equal"""
    if len(lista) != len(listb):
        return False
    if lista == [] and listb == []:
        return True
    for elem in range(
        0, len(lista)
    ):  # used a nested for loop first and realized that didn't work
        if lista[elem] != listb[elem]:
            return False
    return True


def extend(lista: list[int], listb: list[int]) -> None:
    """Extends one list with all the elements in another"""
    for elem2 in listb:
        lista.append(elem2)
