""" Assignment 0 in SC-T308-PRLA """
from itertools import starmap  # islice,
from operator import mul


def sum_two(first, second):
    """ Takes two integers and adds them together. """
    return first + second


def mod_sum(integer):
    """ Takes a range and returns the sum of multiples of 3 or 5 below
    the range. """
    # numbers = [x for x in range(integer) if x % 3 == 0 or x % 5 == 0]
    # return sum(numbers)
    return sum(x for x in range(integer) if x % 3 == 0 or x % 5 == 0)


def sum_no_3(lis):
    """ Takes a list of numbers and adds them together if the last
    digit is not 3. """
    sum_list = []
    for num in lis:
        temp = str(num)
        if temp[-1] != '3':
            sum_list.append(int(temp))
    return sum(sum_list)


def sum_first(lis, integer):
    """ Returns the sum of the first n integers on the list. """
    if len(lis) < integer:
        return sum(lis)
    # temp_list = [x for x in islice(lis, 0, integer)]
    # return sum(temp_list)
    return sum(x for x in lis[0:integer:])


def list_product(lis1, lis2):
    """ Takes two lists a multiplies the same indies together. """
    combined = zip(lis1, lis2)
    return list(starmap(mul, combined))


def remove_empty(lis):
    """ Takes a list of strings and returns the same list without
    empty stings. """
    return [x for x in lis if x != '']


def decrypt(message):
    """ Takes a string and decrypt's it so that it's readable. """
    decrypted = []
    for letter in message[0::3]:
        decrypted.append(letter)
    return ''.join(decrypted)


def gymnastics(lis):
    """ Returns the average of the list. """
    if len(lis) > 2:
        lis = sorted(lis)
        del lis[-1]
        del lis[0]
    return int(sum(lis) / len(lis))


def boom(integer):
    """ Takes an integer and makes a list with each number as a string,
    if the number is divisable by 7 or contains 7 it is replaced by the
    string 'boom!'."""
    final_list = []
    string_list = []
    int_list = [x for x in range(1, integer + 1)]
    for num in int_list:
        if num % 7 == 0:
            string_list.append('boom!')
        else:
            string_list.append(str(num))
    for num in string_list:
        if '7' in num:
            final_list.append('boom!')
        else:
            final_list.append(num)
    return final_list
