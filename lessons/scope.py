def remove_chars(msg: str, char: str) -> str:
    copy: str = ""  # Set up empty str to copy values over
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy = copy + msg[index]
        index += 1
    return copy


word: str = "yoyo"

print(remove_chars(word, "y"))
