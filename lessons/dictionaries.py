"""Introduction to Dictionaries"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

ice_cream["vanilla"] += 110

print(ice_cream)


def reverse(xs: list[str]) -> list[str]:
    """Reverse elements of input list without mutation."""
    reversed: list[str] = []
    idx: int = len(xs) - 1
    while idx >= 0:
        reversed.append(xs[idx])
        idx -= 1
    return reversed


print(reverse([1, 2, 3, 4]))
