"""While Loops Challenge Question"""

__author__ = "730672928"


def num_instances(phrase: str, search_char: str) -> None:
    """Determines if a phrase has a character or not"""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if (
            phrase[index] == search_char
        ):  # initially had this as phrase [count], remember that count is not always updating!
            count = count + 1
            index = index + 1
        else:
            index = index + 1
    print(
        str(count)
    )  # forgot a print statement at first, that's why I was not getting output


# why do we not need a "if" = main here?
