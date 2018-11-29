""" Assignment 01 in SC-T-308-PRLA """
from collections import Counter
from itertools import zip_longest
import re  # RegExp for filtering


def cdo(string):
    """ Takes a string, sortes it and then returns a sorted string. """
    temp = sorted(string.split())
    return ' '.join(temp)


def duplicates(lis):
    """ Takes a list and returns the duplicates in the list. """
    counter = Counter(lis)
    # Here we use the 'Counter' data structure. It keeps track of
    # how many duplicates exist in the structure.
    return [x for x in counter if counter[x] > 1]


def flatten(lis):
    """ Take a list and flatten it. """
    # Here a list containing 0 to length of the list is Zipped together
    # into tuple pairs. Now each element is mapped to an index and is sorted.
    temp_zip = zip(sorted(lis), range(len(lis)))
    # From the tuples we create a hash table mapped to the index value
    # as the keys. This is a dictionary comprehension.
    temp_dict = {k: v for (k, v) in temp_zip}
    # An empty array to keep the return value.
    flat_list = []
    for num in lis:
        # Here using the get() method we call the hash table and
        # append the appropriate value to the new list.
        flat_list.append(temp_dict.get(num))
    return flat_list


def rm_duplicates(lis):
    """ Takes a list, removes duplicates and returns it sorted. """
    a_set = set(lis)
    return sorted(a_set)


def scramble(lis1, lis2):
    """ Takes two lists, one as values and the other as indies. Then sorts
    the value list according to the indies and returns a list. """
    # This is very much like flatten() from above. Only keys and values
    # are reversed.
    temp_zip = zip(range(len(lis1)), lis1)
    temp_dict = {k: v for (k, v) in temp_zip}
    scrambled = []
    for num in lis2:
        scrambled.append(temp_dict.get(num))
    return scrambled


def excel_index(column):
    """ Takes a string and returns what column it would be in Excel. """
    # Not needed but will insure the right values. There are different
    # ASCII values for uppercase and lowercase letters.
    letters = list(column.upper())
    # The power for calculating the the base 26 numbers to decimal.
    power = len(column) - 1
    # A variable to keep the return value.
    column_number = 0
    for letter in letters:
        # This works like this: LOL = 8514
        # 26^2 * 12(L) + 26^1 * 15(O) + 26^0 * 12 = 8514
        column_number += 26**power * (ord(letter) - 64)
        power -= 1
    return column_number


def birthdays(string):
    """ Takes a multiline string and returns the numbers that represent
    the same dates."""
    # Break the string up into an array, sort it and filter out the junk.
    kt_list = string.split()
    kt_sorted = sorted(kt_list)
    kt_filtered = [x for x in kt_sorted if x != '']
    bday_list = []
    # Here we are looking for duplicates in the list.
    for idx_i in kt_filtered:
        for idx_j in kt_filtered:
            # Here we are checking if the first part matches but not the
            # later part. We are looking for same dates but not complete
            # matches.
            if idx_i[0:4] == idx_j[0:4] and idx_i[4:] != idx_j[4:]:
                bday_list.append(idx_i)
                break
    # For the last step we use a Set data structure.
    final_list = set()
    # A nested for loop.
    for kennit in bday_list:
        # A temporary search string for each iteration.
        string = kennit[0:4]
        # A temporary tuple warehouse for each iteration.
        temp = []
        for ktt in bday_list:
            # If there is a match, put it into the temp list.
            if ktt.startswith(string):
                temp.append(ktt)
        # Now we're out of the inner loop, we append the tuple to
        # the final Set list before the next outer iteration.
        final_list.add(tuple(temp))
    return list(final_list)


def process_ls(string):
    """ Takes a multiline string and returns a sorted list. """
    # Start off by making rows
    rows = re.split(r'\n', string)
    # An empty 2D array
    list_list = []
    # Then go to work on each row...
    for row in rows:
        # Clean out all whitespace pollution, substitute with '?'.
        # The '?' is a good choice because it will never appear in
        # the string naturally.
        temp_string = re.sub(r'(\s\s)|(\s{1}[^-]\s{1})', '?', row)
        # Split the row on each '?' in the string.
        temp_list = re.split(r'\?', temp_string)
        # Next append each row as a second demension into the 2D array.
        list_list.append([x.strip() for x in temp_list if x != ''])
    # Now with a 'clean' 2D array it needs to be flattened.
    # Using the unpack operator and fancy itertools a list of tuples
    # is generated. Each tuple holds the right order of items.
    semi_processed = list(zip_longest(*list_list, fillvalue='?'))
    # Setting up the final step. Create an empty array to populate.
    processed_list = []
    # With nested loops we iterate through everything and
    # append each item to the new list.
    for index, _ in enumerate(semi_processed):
        for item in semi_processed[index]:
            # Here I skip adding '?' to the list.
            if item.find('?') == -1:
                # Each item is appended to the list.
                processed_list.append(item)
    return processed_list
