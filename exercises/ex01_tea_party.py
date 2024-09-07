"""My first real exercise in COMP110!"""

__author__: str = "730672928"


# I noticed that for this function, the last print statement automatically formatted itself repeatedly even though I keep reformatting it
def main_planner(guests: int) -> None:
    """This function links all the others together"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """This function will compute the number of tea bags"""
    return people * 2


def treats(people: int) -> int:
    """This function will return the number of treats"""
    return int((tea_bags(people=people)) * 1.5)


# I was initially confused how this function would operate with seperate variables but I understood it when it all came together!
def cost(tea_count: int, treat_count: int) -> float:
    """This function computes the cost of the tea party"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
