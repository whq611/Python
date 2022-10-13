"""
https://en.wikipedia.org/wiki/Floor_and_ceiling_functions
"""
import math

def floor(x: float) -> int:
    """
    Return the floor of x as an Integral.
    :param x: the number
    :return: the largest integer <= x.
    >>> import math
    >>> all(floor(n) == math.floor(n) for n
    ...     in (1, -1, 0, -0, 1.1, -1.1, 1.0, -1.0, 1_000_000_000))
    True
    """
    return math.floor(x)


n=float(input("Enter the number"))
print(floor(n))
