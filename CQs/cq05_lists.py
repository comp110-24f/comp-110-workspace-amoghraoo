"""Mutating functions."""

__author__ = "730672928"


def manual_append(lista: list[int], valuea: int) -> None:
    lista.append(valuea)
    print(lista)


def double(listb: list[int]) -> None:
    index: int = 0
    while index < len(listb):
        listb[index] *= 2
        index += 1
    print(listb)


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
