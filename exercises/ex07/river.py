"""File to define River class."""

__author__ = "730672928"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Defines class River."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of fish and bears."""
        index = (
            len(self.fish) - 1
        )  # I realized that I would have to loop backwards inorder to use the pop function to not misnumber the index
        while index >= 0:
            if self.fish[index].age > 3:
                self.fish.pop(index)
            index -= 1
        index = len(self.bears) - 1
        while index >= 0:
            if self.bears[index].age > 5:
                self.bears.pop(index)
            index -= 1
        return None

    def remove_fish(self, amount: int):
        """Removes the first fish."""
        for _ in range(amount):
            if self.fish:
                self.fish.pop(0)
        return None

    def bears_eating(self):
        """Simulates the bears eating."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Checks what bears are left based on the hunger score."""
        bears_left = (
            []
        )  # I tried implementing a pop method here but kept running into index errors and an infinite loop so I decided to switch
        for bear in self.bears:
            if bear.hunger_score >= 0:
                bears_left.append(bear)
        self.bears = bears_left
        return None

    def repopulate_fish(self):
        """Reproduces the fish."""
        new_fish = (len(self.fish) // 2) * 4
        for _ in range(
            new_fish
        ):  # I saw how the for loops were defined above and how we can have a for loop without a defined variable within it.
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Reproduces the bear."""
        new_bears = len(self.bears) // 2
        for _ in range(new_bears):
            self.bears.append(Bear())
        return None  # is there a difference between using a return statement and not? I forgot on one of them and it still worked.

    def view_river(self):
        """Allows us to view the river at the current day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates the river for a week."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
