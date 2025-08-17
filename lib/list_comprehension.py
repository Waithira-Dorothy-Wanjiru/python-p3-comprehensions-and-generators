#!/usr/bin/env python3

def return_evens(num_list):
    """
    Returns a list of all even numbers from the given list of integers.
    Example:
    return_evens([0, 1, 3, 5, 7, 8, 9]) -> [0, 8]
    """
    return [n for n in num_list if n % 2 == 0]


def make_exclamation(sentence_list):
    """
    Returns a list of sentences with exclamation marks at the end.
    Example:
    make_exclamation(["Hello", "I'm doing great", "Python is fun"])
    -> ["Hello!", "I'm doing great!", "Python is fun!"]
    """
    return [s + "!" for s in sentence_list]
