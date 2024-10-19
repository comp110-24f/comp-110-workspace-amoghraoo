"""Finding a max in the list"""

__author__ = 730672928


def find_and_remove_max(a: list[int]) -> int:
    if a == []:
        return -1
    compare: int = a[0]
    idx: int = 0
    while idx < len(a):
        if a[idx] > compare:
            compare = a[idx]
        idx += 1
    idx = 0
    while idx < len(a):
        if a[idx] == compare:
            a.pop(idx)
        else:
            idx += 1
    return compare
