"""File to define Fish class."""

__author__ = "730703450"


class Fish:
    """Represents fish in a river ecosystem."""

    age: int

    def __init__(self):
        """Initializes fish with age."""
        self.age = 0
        return None

    def one_day(self):
        """Simulates one day as a fish."""
        self.age += 1
        return None
