"""File to define Bear class."""

__author__ = "730703450"


class Bear:
    """Represents bear in a river ecosystem."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes bear class with age and hunger score."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Simulates one day for bear."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Increase hunger score by # of fish eaten."""
        self.hunger_score += num_fish
        return None
