""" Largest product in a series

The four adjacent digits in the 1000-digit number that have the
greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that
have the greatest product. What is the value of this product?"""

from functools import reduce

# =============
# Program start
# =============

# 20 x 50 number strings.
STRING1 = '73167176531330624919225119674426574742355349194934'
STRING2 = '96983520312774506326239578318016984801869478851843'
STRING3 = '85861560789112949495459501737958331952853208805511'
STRING4 = '12540698747158523863050715693290963295227443043557'
STRING5 = '66896648950445244523161731856403098711121722383113'
STRING6 = '62229893423380308135336276614282806444486645238749'
STRING7 = '30358907296290491560440772390713810515859307960866'
STRING8 = '70172427121883998797908792274921901699720888093776'
STRING9 = '65727333001053367881220235421809751254540594752243'
STRING10 = '52584907711670556013604839586446706324415722155397'
STRING11 = '53697817977846174064955149290862569321978468622482'
STRING12 = '83972241375657056057490261407972968652414535100474'
STRING13 = '82166370484403199890008895243450658541227588666881'
STRING14 = '16427171479924442928230863465674813919123162824586'
STRING15 = '17866458359124566529476545682848912883142607690042'
STRING16 = '24219022671055626321111109370544217506941658960408'
STRING17 = '07198403850962455444362981230987879927244284909188'
STRING18 = '84580156166097919133875499200524063689912560717606'
STRING19 = '05886116467109405077541002256983155200055935729725'
STRING20 = '71636269561882670428252483600823257530420752963450'

# Combining all 20 strings into one 1000 digit long string.
THOUSAND_STRING = (STRING1 +
                   STRING2 +
                   STRING3 +
                   STRING4 +
                   STRING5 +
                   STRING6 +
                   STRING7 +
                   STRING8 +
                   STRING9 +
                   STRING10 +
                   STRING11 +
                   STRING12 +
                   STRING13 +
                   STRING14 +
                   STRING15 +
                   STRING16 +
                   STRING17 +
                   STRING18 +
                   STRING19 +
                   STRING20)

# Creating an immutable tuple to work with each digit. Total length = 1000.
THOUSAND = tuple(THOUSAND_STRING)

''' The API function should take an integer that represents how many
adjacent digits should be checked for the greatest product. '''

# Defining a function to look at the 13 digits in the interval.


def look_at_13(start):
    # Using a list comprehension to get index of the tuple.
    interval = list(i for i in range(start, start+13))
    # Mapping the values from the indices in the list.
    numbers = list(map(lambda n: int(THOUSAND[n]), interval))
    # And finally reducing each 13 space interval to find its product.
    return reduce(lambda acc, val: acc*val, numbers, 1)

# The function that looks at the 1000 digit number.


def look_at_1000():
    # Two local variables to keep the highest seen product and its starting index.
    highest = 0
    index = 0
    # The ranged loop to iterate the 1000 digits.
    for val in range(988):
        # Calling the interval reducer function.
        current = look_at_13(val)
        # Looking for the highest value and its starting index.
        if current > highest:
            highest = current
            index = val
    # Finally returning the greatest product and where it's seated.
    return dict({'Hi-Product': highest, 'Interval': [index, index+12]})


print(look_at_1000())
