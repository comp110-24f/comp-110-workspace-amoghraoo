"""Practice with conditionals."""


def less_than_10(num: int) -> None:
    """Tell me if num is less than 10."""
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day.")


less_than_10(num=3)


def check_first_letter(word: str, letter: str) -> str:
    """Will tell us if a letter and the first letter of a word are the same."""
    if (word[0]) == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="s"))
