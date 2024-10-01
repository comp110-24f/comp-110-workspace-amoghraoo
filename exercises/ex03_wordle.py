"""Wordle: A simpler python version."""

__author__ = "730672928"


def input_guess(
    secret_word_len: int,
) -> (
    str
):  # it was hard for me to figure out what variable names to use given they kept repeating
    """Checks if inputed word is of correct length."""
    guess_word: str = input(f"Enter a {secret_word_len} character word: ")
    while secret_word_len != len(guess_word):
        guess_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess_word


def contains_char(secret_word: str, guess_char: str) -> bool:
    """Checks if word contains a guessed character."""
    assert (
        len(guess_char) == 1
    )  # Asserting that the length of the guess_char can only be 1
    index1: int = 0
    count1: int = 0
    while index1 < len(secret_word):
        if secret_word[index1] == guess_char:
            index1 += 1
            count1 += 1
        else:
            index1 += 1
    if count1 > 0:
        return True
    else:
        return False


def emojified(user_guess: str, secret: str) -> str:
    """Determines how close guess is relative to secret using emojis."""
    assert len(user_guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    output: str = ""  # creating an empty string
    while index < len(
        user_guess
    ):  # I first created two while loops, but soon realized that would not work
        if user_guess[index] == secret[index]:
            output += GREEN_BOX
        elif contains_char(secret, user_guess[index]) == True:
            output += YELLOW_BOX
        else:
            output += WHITE_BOX
        index += 1
    return output


def main(secretword: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    result: bool = False
    while turns <= 6 and not result == True:
        print(
            f"=== Turn {turns}/6 ==="
        )  # I learned that you can use interger variables using this notation without converting them to strings!
        input_word: str = input_guess(
            secret_word_len=len(secretword)
        )  # intitially I did not have a local variable and was confused how to recieve the user input and use it in this function
        print(emojified(input_word, secretword))
        if secretword == input_word:
            result = True
        else:
            turns += 1
    if result == True:
        print(f"You won in {turns}/6 turns!")
    else:
        print(
            "X/6 - Sorry, try again tomorrow!"
        )  # I initially used the exit() function and realized that the autograder did not accept that


if __name__ == "__main__":
    main(secretword="codes")
