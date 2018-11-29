""" Assignment 01 in SC-T-308-PRLA """
from collections import Counter
from itertools import zip_longest
import re


def cdo(string):
    """ Takes a string, sortes it and then returns a sorted string. """
    temp = sorted(string.split())
    return ' '.join(temp)


def duplicates(lis):
    """ Takes a list and returns the duplicates in the list. """
    counter = Counter(lis)
    return [x for x in counter if counter[x] > 1]


def flatten(lis):
    """ Take a list and flatten it. """
    temp_zip = zip(sorted(lis), range(len(lis)))
    temp_dict = {k: v for (k, v) in temp_zip}
    flat_list = []
    for num in lis:
        flat_list.append(temp_dict.get(num))
    return flat_list


def rm_duplicates(lis):
    """ Takes a list, removes duplicates and returns it sorted. """
    a_set = set(lis)
    return sorted(a_set)


def scramble(lis1, lis2):
    """ Takes two lists, one as values and the other as indies. Then sorts
    the value list according to the indies and returns a list. """
    temp_zip = zip(range(len(lis1)), lis1)
    temp_dict = {k: v for (k, v) in temp_zip}
    scrambled = []
    for num in lis2:
        scrambled.append(temp_dict.get(num))
    return scrambled


def excel_index(column):
    """ Takes a string and returns what column it would be in Excel. """
    letters = list(column.upper())
    power = len(column) - 1
    column_number = 0
    for letter in letters:
        column_number += 26**power * (ord(letter) - 64)
        power -= 1
    return column_number


def birthdays(string):
    """ Takes a multiline string and returns the numbers that represent
    the same dates."""
    kt_list = string.split()
    kt_filtered = [x for x in kt_list if x != '']
    kt_filtered = sorted(kt_filtered)
    bday_list = []
    for idx_i in kt_filtered:
        for idx_j in kt_filtered:
            if idx_i[0:4] == idx_j[0:4] and idx_i[4:] != idx_j[4:]:
                bday_list.append(idx_i)
                break
    final_list = set()
    for kennit in bday_list:
        string = kennit[0:4]
        temp = []
        for ktt in bday_list:
            if ktt.startswith(string):
                temp.append(ktt)
        final_list.add(tuple(temp))
    return list(final_list)


def process_ls(string):
    """ Takes a multiline string and returns a sorted list. """
    rows = re.split(r'\n', string)
    list_list = []
    for row in rows:
        temp_string = re.sub(r'(\s\s)|(\s{1}[^-]\s{1})', '?', row)
        temp_list = re.split(r'\?', temp_string)
        list_list.append([x.strip() for x in temp_list if x != ''])
    semi_processed = list(zip_longest(*list_list, fillvalue='?'))
    processed_list = []
    for index, _ in enumerate(semi_processed):
        for item in semi_processed[index]:
            if item.find('?') == -1:
                processed_list.append(item)
    return processed_list
