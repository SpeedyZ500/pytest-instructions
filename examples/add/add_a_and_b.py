from typing import Collection


def add_a_and_b(a, b):
    if isinstance(a, (str | Collection)) or isinstance(b, (str | Collection)):
        raise TypeError("must be a numeric value")
    return a + b