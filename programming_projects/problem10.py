""" Summation of primes
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million."""

import math
from functools import reduce


def is_prime_v3(integer):
    # Version three of the "is_prime function". It is really quick.
    """Return 'True' if integer is a prime. Else 'False'."""
    if integer == 0:
        return False
    if integer == 1:
        return False
    if integer == 2:
        return True
    if integer > 2 and integer % 2 is 0:
        return False
    max_divisor = math.floor(math.sqrt(integer))
    for number in range(3, 1 + max_divisor, 2):  # (start|stop|increments)
        if integer % number == 0:
            return False
    return True


# First get a list of all the primes under two million.
primes_under_2mill = list(x for x in range(1, 2000000) if is_prime_v3(x))

# With the reduce function sum a the intergers in the list.
sum_of_prime = reduce(lambda acc, val: acc + val, primes_under_2mill)

# Print out the total sum.
print(sum_of_prime)
