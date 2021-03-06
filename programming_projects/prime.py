""" Playing around with code from Socratia || Python Tutorials
https://www.youtube.com/playlist?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er- """
import math
from time import time

# ==============
# Prime checkers
# ==============


def is_prime_v1(integer):
    """Return 'True' if integer is a prime. Else 'False'."""
    if integer == 0:
        return False
    if integer == 1:
        return False  # 1 is a unit, not a prime
    for number in range(2, integer):
        if integer % number is 0:
            return False  # The number has a divisor other than itself and one.
    return True


def is_prime_v2(integer):
    """Return 'True' if integer is a prime. Else 'False'."""
    if integer == 0:
        return False
    if integer == 1:
        return False
    max_divisor = math.floor(math.sqrt(integer))
    for number in range(2, 1 + max_divisor):
        if integer % number is 0:
            return False
    return True


def is_prime_v3(integer):
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

# =================
# Utility functions
# =================


def timer(version, end_value):
    """ Asks for the version(1 or 2 or 3) you want to time and the end value
    and prints out the total time taken to compute the prime numbers in the
    interval."""
    if version == 1:
        time_0 = time()
        for number in range(1, end_value):
            is_prime_v1(number)
        time_1 = time()
        print('Time required:', time_1 - time_0, 'seconds')
    elif version == 2:
        time_0 = time()
        for number in range(1, end_value):
            is_prime_v2(number)
        time_1 = time()
        print('Time required:', time_1 - time_0, 'seconds')
    elif version == 3:
        time_0 = time()
        for number in range(1, end_value):
            is_prime_v3(number)
        time_1 = time()
        print('Time required:', time_1 - time_0, 'seconds')
    else:
        print('There is no version', version)

# timer(3, 500000)


def tester():
    """ Tests by printing out the prime numbers between [1 and 20)."""
    for number in range(1, 21):
        print(number, is_prime_v3(number))

# tester()

# ==============
# Data functions
# ==============


def list_the_primes(numbers):
    """Returns a list with all the prime numbers up to and including the number
    passed in as the argument."""
    # List comprehension method > Smooth one liner
    return list(number for number in range(numbers + 1) if is_prime_v3(number))

# print(list_the_primes(20))


''' Below is a command line tool that takes an integer as an input and returns
    either "True" if the integer is a prime number or "False" if it is not. '''

print('Enter a number to see if it is a prime number: ')
INPUT_NUMBER = input()
print(is_prime_v3(int(INPUT_NUMBER)))
