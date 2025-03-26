"""Exercise about dictionaries"""

__author__ = "730703450"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """inverts the inputed dictionary"""
    inverted_dict: dict[str, str] = {}
    for key in dictionary:
        inv_dict_key = dictionary[key]
        if inv_dict_key in inverted_dict:
            raise KeyError("no duplicate words")
        inverted_dict[inv_dict_key] = key
    return inverted_dict


def count(list: list[str]) -> dict[str, int]:
    """returns a dict where keys are strs and values are # of occurences"""
    counter: dict[str, int] = {}
    count: int = 0
    for item in list:
        if item in counter:
            count = counter[item] + 1
        else:
            count = 1
        counter[item] = count
    return counter


def favorite_color(colors: dict[str, str]) -> str:
    """input dict of name with fav colors, returns string of most common color"""
    max: int = 0
    counter: dict[str, int] = {}
    most_frequent: str = ""
    for name in colors:
        count: int = 0
        if colors[name] in colors.values() and colors[name] not in counter:
            count += 1
        if colors[name] in counter:
            count = counter[colors[name]] + 1
        counter[colors[name]] = count
    for color in counter:
        if counter[color] > max:
            max = counter[color]
            most_frequent = color
    return most_frequent


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """bins words by length"""
    result: dict[int, set[str]] = {}
    i: int = 0
    while i < len(words):
        if len(words[i]) in result:
            result[len(words[i])].add(words[i])
        else:
            result[len(words[i])] = set([words[i]])
        i += 1
    return result
