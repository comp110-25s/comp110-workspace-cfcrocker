"""tests for functions defined in dictionary.py"""

__author__ = "730703450"


from exercises.ex03.dictionary import invert, favorite_color, count, bin_len

# change some maybe ish -- variable names and ish


# edge case for invert
def test_invert_empty() -> None:
    """tests reult when empty dictionary is given"""
    dictionary: dict[str, str] = {}
    assert invert(dictionary) == {}


# use cases for invert
def test_invert_multi() -> None:
    """tests return of dictionary when multiple items are switched"""
    dictionary: dict[str, str] = {"a": "b", "c": "d", "e": "f"}
    assert invert(dictionary) == {"b": "a", "d": "c", "f": "e"}


def test_invert_two() -> None:
    """test return of dictionary when only two items are switched"""
    dictionary: dict[str, str] = {"one": "two", "goodbye": "bye"}
    assert invert(dictionary) == {"two": "one", "bye": "goodbye"}


# edge case for favorite color
def test_favorite_color_empty() -> None:
    """tests return of fav color when given dict is empty"""
    colors: dict[str, str] = {}
    assert favorite_color(colors) == ""


def test_favorite_color_two() -> None:
    """Tests fav color string when two are most common"""
    colors: dict[str, str] = {
        "one": "pink",
        "two": "purple",
        "three": "purple",
        "four": "pink",
    }
    assert favorite_color(colors) == "pink"


def test_favorite_color_one() -> None:
    """tests fav color when one is most common"""
    colors: dict[str, str] = {"one": "silver", "two": "green", "three": "silver"}
    assert favorite_color(colors) == "silver"


# edge case for count
def test_count_empty() -> None:
    """tests count function when list is empty"""
    list: list[str] = []
    assert count(list) == {}


# use cases for count
def test_count_multi() -> None:
    """tests count when multiple list items are inputed"""
    list: list[str] = ["one", "two", "two", "three", "three", "three"]
    assert count(list) == {"one": 1, "two": 2, "three": 3}


def test_count_same() -> None:
    """tests count when all list items are the same"""
    list: list[str] = ["five", "five", "five", "five", "five"]
    assert count(list) == {"five": 5}


# edge case for bin len
def test_bin_len_empty() -> None:
    """tests bin len function when list is empty"""
    words: list[str] = []
    assert bin_len(words) == {}


# use cases for bin len
def test_bin_len_diff() -> None:
    """tests bin len when they are all different words"""
    assert bin_len(["pit", "flats", "pot"]) == {3: {"pit", "pot"}, 5: {"flats"}}


def test_bin_len_sae() -> None:
    """tests bin len when all words are the same words"""
    assert bin_len(["the", "the", "the"]) == {3: {"the"}}
