"""File to define River class."""

__author__ = "730703450"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """River class."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

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
        """Checks ages."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]
        return None

    def remove_fish(self, amount: int):
        """Removes fish."""
        self.fish = self.fish[amount:]

    def bears_eating(self):
        """Simulates bears eating."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self):
        """Checks hunger of bear."""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        return None

    def repopulate_fish(self):
        """Repopulates fish."""
        new_fish = (len(self.fish) // 2) * 4
        self.fish.extend([Fish() for _ in range(new_fish)])
        return None

    def repopulate_bears(self):
        """Repopulates bears."""
        new_bears = len(self.bears) // 2
        self.bears.extend([Bear() for _ in range(new_bears)])
        return None

    def view_river(self) -> None:
        """View river stats."""
        return print(
            f"~~~ Day {self.day}: ~~~\n"
            f"Fish population: {len(self.fish)}\n"
            f"Bear population: {len(self.bears)}"
        )

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
        """Simulate one week of life in the river."""
        for _ in range(7):
            self.one_river_day()
