"""Coordinates CQ04"""

__author__ = "730672928"


def get_coords(xs: str, ys: str) -> None:
    index1: int = 0
    index2: int = 0
    coordinate: str = ""
    while index1 < len(xs):
        index2 = 0
        while index2 < len(ys):
            coordinate = "(" + xs[index1] + "," + ys[index2] + ")"
            print(coordinate)
            index2 += 1
        index1 += 1
