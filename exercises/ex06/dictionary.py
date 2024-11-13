"""Dictionary utility functions"""

__author__ = "730672928"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values"""
    resultdict: dict[str, str] = {}
    resultkey: str = ""
    for key in input:
        resultkey = input[key]
        if (
            resultkey in resultdict
        ):  # wasn't sure at first how we would raise error so had to look back at another exersize
            raise KeyError("Duplicate key, try again")
        resultdict[resultkey] = key
    return resultdict


def favorite_color(input: dict[str, str]) -> str:
    """Returns the most popular color"""
    colorlist: list[str] = []
    current_item: str = ""
    max_count: int = 0
    most_common_item: str = ""
    for key in input:
        colorlist.append(input[key])
    for idx in range(len(colorlist)):
        current_item = colorlist[idx]
        count: int = 0
        for idx2 in range(len(colorlist)):
            if colorlist[idx2] == current_item:
                count += 1
        if (
            count > max_count
        ):  # realized I needed another variable that could parse through the max_count to compare
            max_count = count
            most_common_item = current_item
    return most_common_item  # is there a way to make this simpler? May have overcomplicated things...


def count(input: list[str]) -> dict[str, int]:
    """Gives the counts of number of times that value appeared in the input list"""
    resultdict: dict[str, int] = {}
    for elem in input:
        if elem in resultdict:
            resultdict[
                elem
            ] += 1  # The syntax for dicts with subscription notation can be a little confusing!
        else:
            resultdict[elem] = 1
    return resultdict


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Returns the list of words that begin with a letter"""
    resultdict: dict[str, list[str]] = {}
    for elem in input:
        first_letter = elem[0].lower()
        if first_letter in resultdict:
            resultdict[first_letter].append(elem)
        else:
            resultdict[first_letter] = [elem]
    return resultdict


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    """Mutate and return attendance"""
    if day in input:
        if student not in input[day]:
            input[day].append(student)
    else:
        input[day] = [student]
    return None  # was simpler than I thought it was going to be!
