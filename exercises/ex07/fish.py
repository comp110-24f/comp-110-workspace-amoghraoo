"""File to define Fish class."""


class Fish:
    """Defines class Fish."""

    age: int

    def __init__(self):
        """Initializes variables."""
        self.age: int = 0
        return None

    def one_day(self):
        """Modulates what happens during one day for Fish."""
        self.age += 1
        return None
