"""Guess the word"""

__author__: str = "730703450"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    x: int = 1  # x is the number of turns that have been used
    right_word: bool = False
    while x <= 6 and right_word is False:
        print(f"=== Turn {x}/6===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            right_word = True
        else:
            x += 1
    if right_word is True:
        print(f"You won in {x}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


def contains_char(word: str, letter: str) -> bool:
    """searches the word for a certain letter"""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    idx: int = 0
    while idx < len(word):
        if letter == word[idx]:
            return True
        idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """compares the correctness between the guessed word and codeword"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"  # constants denoted in all caps
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""  # this empty string will be appended onto
    idx: int = 0
    while idx < len(secret):
        if guess[idx] == secret[idx]:  # compares the came indices of each word
            result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        idx += 1
    return result


def input_guess(n: int) -> str:
    """prompts for a guess and continues til a word of the expected length is entered"""
    guess_word: str = input(f"Enter a {n} character word:")
    while n != len(guess_word):
        input(
            f"That wasn' {n} chars! Try again:"
        )  # if # of characters in word doesn't match exp length, it'll return message
    return guess_word
