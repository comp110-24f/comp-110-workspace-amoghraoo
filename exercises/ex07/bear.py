"""File to define Bear class."""


class Bear:
    """Defines class Bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes Variables."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None

    def one_day(self):
        """Changes for one day for bear."""
        self.age += 1
        self.hunger_score -= 1  # I was so used to doing += that I forgot -= is also a valid construction!
        return None

    def eat(self, num_fish: int):
        """Modulates what happends when the bear eats."""
        self.hunger_score += num_fish
