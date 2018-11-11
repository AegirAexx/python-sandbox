
''' Smallest multiple
    2520 is the smallest number that can be divided by each of the
    numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible
    by all of the numbers from 1 to 20? '''

import math

# Straight up Brute force method: Runtime is about 15 minutes.

# def modulo(index, num):
#     acc = 0
#     for x in range(num):
#         acc += num % (x + 1)
#     return acc == 0

# def find_that_number(num):
#     index_i = 1
#     while(True):
#         if modulo(index_i, num):
#             break
#         index_i += 1
#     return index_i

# print(find_that_number(20))

''' A much more sophisticated method using mathematics:
    https://en.wikipedia.org/wiki/Least_common_multiple
    https://en.wikipedia.org/wiki/Euclidean_algorithm '''

# Uses 'log' from 'math'
# Runtime is less than one second.

def find_the_primes_1(pool_of_primes):
    ''' Finds all the primes in the number range and returns them in a list'''
    prime_numbers = []
    index_i = 2
    while index_i < (pool_of_primes + 1):
        index_j = 2
        while index_j <= (index_i/index_j):
            if not index_i % index_j:
                break
            index_j += 1
        if index_j > index_i / index_j:
            prime_numbers.append(index_i)
        index_i += 1
    return prime_numbers

def least_common_multiple_1(number):
    ''' Return the least common multiple number '''
    lcm = 1
    for prime in find_the_primes_1(number):
        lcm *= prime**(math.log(number, prime)//1)
    return int(lcm)

print(least_common_multiple_1(20))
