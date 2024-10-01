"""Practice with lists."""

my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = []  # literal

my_numbers.append(1.5)

game_points: list[int] = [102, 86, 94]


# print(my_numbers)
# print(game_points)

grocery_list: list[str] = ["eggs", "milk", "bananas"]
grocery_list.pop(2)

# print(grocery_list)


def display(list_a: list[int]) -> None:
    index: int = 0
    while index < len(list_a):
        print(list_a[index])
        index += 1


display(list_a=game_points)
