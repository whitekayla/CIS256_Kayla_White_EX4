# Kayla White — CIS256 — EX4
# Tests for my Guess the Word game.
# These make sure my game logic is working the way it's supposed to.

import random
import guess_the_word as gw

def test_word_is_from_list():
    # Setting a seed makes the test consistent every time it's run
    random.seed(7)
    word = gw.select_word(gw.WORDS)
    assert word in gw.WORDS

def test_correct_guess_updates_state():
    secret = "loop"
    current = ["_"] * len(secret)
    guessed = set()

    # Guessing 'o' should reveal both 'o's in the word
    new_state, correct, repeat = gw.process_guess(secret, current, "o", guessed)

    assert correct is True
    assert repeat is False
    assert new_state == ["_", "o", "o", "_"]

def test_incorrect_guess_does_not_change_state():
    secret = "array"
    current = ["_"] * len(secret)
    guessed = set()

    # 'z' is not in array, so nothing should change
    new_state, correct, repeat = gw.process_guess(secret, current, "z", guessed)

    assert correct is False
    assert repeat is False
    assert new_state == ["_", "_", "_", "_", "_"]

def test_repeat_guess_is_detected():
    secret = "tuple"
    current = ["_"] * len(secret)
    guessed = set()

    # First guess of 't' should update the word
    state1, correct1, repeat1 = gw.process_guess(secret, current, "t", guessed)
    # Guessing 't' again should be marked as a repeat
    state2, correct2, repeat2 = gw.process_guess(secret, state1, "t", guessed)

    assert correct1 is True
    assert repeat1 is False
    assert repeat2 is True
    assert state2 == state1  # No changes on repeat guess
