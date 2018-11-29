""" Assignment 0 in SC-T308-PRLA """
from itertools import starmap
from operator import mul


def sum_two(first, second):
    """ Takes two integers and adds them together. """
    return first + second


def mod_sum(integer):
    """ Takes a range and returns the sum of multiples of 3 or 5 below
    the range. """
    return sum(x for x in range(integer) if x % 3 == 0 or x % 5 == 0)


def sum_no_3(lis):
    """ Takes a list of numbers and adds them together if the last
    digit is not 3. """
    return sum(x for x in lis if x % 10 != 3)


def sum_first(lis, integer):
    """ Returns the sum of the first n integers on the list. """
    if len(lis) < integer:
        return sum(lis)
    return sum(x for x in lis[0:integer:])


def list_product(lis1, lis2):
    """ Takes two lists a multiplies the same indies together. """
    return list(starmap(mul, zip(lis1, lis2)))


def remove_empty(lis):
    """ Takes a list of strings and returns the same list without
    empty stings. """
    return [x for x in lis if x != '']


def decrypt(message):
    """ Takes a string and decrypt's it so that it's readable. """
    decrypted = [x for x in message[::3]]
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
    string_list = []
    for num in range(1, integer + 1):
        if num % 7 == 0:
            string_list.append('boom!')
        else:
            string_list.append(str(num))
    for idx in range(len(string_list)):
        if string_list[idx].find('7') != -1:
            string_list[idx] = 'boom!'
    return string_list
