"""Chardle (a step towards wordle) in Python! My second exercize."""

__author__ = "730672928"


def input_word() -> str:
    """Checks the inputed word."""
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        print("'" + word + "'")
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()


def input_letter() -> str:
    """Checks the inputed letter."""
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        print(
            "'" + letter + "'"
        )  # I experimented to see if returning the function would give us the format required but it seems like this is necessary
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(check_word: str, check_letter: str) -> None:
    """Searches for the letter in the word."""
    print("Searching for " + check_letter + " in " + check_word)
    index: int = 0
    count: int = 0
    if len(check_word) == 5:
        while (
            index < 5
        ):  # while knowing that I could us a while or if statement, I tried with if first and found it very complicating! Loops help simplify the program.
            if check_word[index] == check_letter:
                print(check_letter + " found at index " + str(index))
                index = index + 1
                count = count + 1
                # This kept formatting itself no matter how long I tried!
            else:
                index = index + 1
                # These variable names are lengthy and make the code longer. I hope to use simpler variable names next time.
    if count == 1:
        print(
            str(count) + " instance of " + check_letter + " found in " + check_word
        )  # I first included this print statement in the if block and I noticed that the count kept printing. That's when I knew to change it.
    elif 1 < count < 5:  # is this the best way to differentiate count instances?
        print(str(count) + " instances of " + check_letter + " found in " + check_word)
    else:
        print("No instances of " + check_letter + " found in " + check_word)


def main() -> None:
    """Calls the function."""
    contains_char(check_word=input_word(), check_letter=input_letter())


if __name__ == "__main__":
    main()
