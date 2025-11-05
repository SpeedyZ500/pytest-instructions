from typing import Collection


def add_a_and_b(a, b):
    if isinstance(a, (str | Collection)) or isinstance(b, (str | Collection)):
        raise TypeError("must be a numeric value")
    return a + b

def same_signs(a: int|float, b: int|float) -> bool:
    if not isinstance(a, int|float) or not isinstance(b, int|float):
        raise TypeError("must be a numeric value")
    return (a < 0 and b < 0) or (a >= 0 and b >=0)

