# Kayla White CIS256  EX4
# Guess the Word Game
# Clean and easy to follow so it’s simple and fun to play.

import random
from typing import List, Tuple, Set

# Class-related words. The game will randomly pick one each time.
WORDS: List[str] = [
    "python", "array", "tuple", "loop",
    "string", "variable", "function", "boolean"
]

# ---------------- Helper Functions ----------------

def select_word(candidates: List[str] = WORDS) -> str:
    """
    Picks a random word from the list.
    Tests can set random.seed outside this function when needed.
    """
    return random.choice(candidates)

def reveal_letters(secret: str, current: List[str], guess: str) -> List[str]:
    """Reveals the positions where the guessed letter actually belongs."""
    for i, ch in enumerate(secret):
        if ch == guess:
            current[i] = guess
    return current

def process_guess(
    secret: str,
    current: List[str],
    guess: str,
    guessed: Set[str]
) -> Tuple[List[str], bool, bool]:
    """
    Handles one letter guess at a time.
    Returns status to help the game respond correctly:
      - updated version of the word
      - whether the guess was correct
      - whether the player already tried that letter
    """
    guess = guess.lower()

    if guess in guessed:
        return current, (guess in secret), True

    guessed.add(guess)

    if guess in secret:
        return reveal_letters(secret, current, guess), True, False

    return current, False, False

def is_word_guessed(current: List[str]) -> bool:
    """If we have no more blanks left, the word is solved."""
    return "_" not in current

# ---------------- Game Play Logic ----------------

def play() -> None:
    print("Welcome to my game! We’re guessing a word from class terms. Let’s win because that’s what we do!")

    secret = select_word()
    current = ["_"] * len(secret)
    attempts = 6
    guessed: Set[str] = set()

    print(f"\nI’m thinking of a {len(secret)}-letter programming word.")
    print("Guess one letter at a time. Type 'quit' if you want to stop.\n")

    while attempts > 0 and not is_word_guessed(current):
        print(f"Word: {' '.join(current)} | Attempts: {attempts} | Guessed: {', '.join(sorted(guessed)) or '-'}")
        guess = input("Enter a letter: ").strip().lower()

        if guess == "quit":
            print("Thanks for playing! Come back anytime.")
            return

        if len(guess) != 1 or not guess.isalpha():
            print("Just one valid letter please.\n")
            continue

        current, correct, repeat = process_guess(secret, current, guess, guessed)

        if repeat:
            print("You already tried that one!\n")
        elif correct:
            print("Yesss! That letter is in the word.\n")
        else:
            attempts -= 1
            print("Nope. Try again.\n")

    if is_word_guessed(current):
        print(f"🎉 You did it! The word was: {secret}")
    else:
        print(f"You ran out of tries! The word was: {secret}. Thanks for giving it a shot!")

if __name__ == "__main__":
    play()
