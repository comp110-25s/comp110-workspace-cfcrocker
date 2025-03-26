"""This program plans a tea party by calculating supplies needed and expected cost"""

__author__: str = "730703450"


def main_planner(guests: int) -> None:
    """Function is the entrypoint for this program"""
    print("A Cozy Tea Party for", (guests), "People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Computes the # of tea bags needed based on # of guests."""
    return people * 2


def treats(people: int) -> int:
    """Computes the # of treats needed based on # of teas guests will drink"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """compute the cost of tea bags and treats combined."""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
