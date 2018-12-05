from itertools import chain
from collections import Counter


def jam(multi_line_string):
    """ See the project description."""

    # Split the long multi line string by lines into an array.
    lines_array = multi_line_string.splitlines()

    # Looping through each line and split them into a second demension array.
    second_demension = [word.split(',') for word in lines_array]

    # Defining the range of the outer loop.
    outer_loop = range(len(second_demension))

    # The outer loop.
    for index_i in outer_loop:
        # Delete the date part
        del second_demension[index_i][-1]
        # Delete the location
        del second_demension[index_i][0]

        # Defining the range of the inner loop.
        inner_loop = range(len(second_demension[index_i]))

        # The inner loop.
        for index_j in inner_loop:
            # Here we overwrite each name variable with a cleaned up version.
            # This is pretty hacky and could be cleaned up alot.
            # It basically does 4 replacement jobs and strips whitespace.
            second_demension[
                index_i][index_j] = second_demension[
                    index_i][index_j].replace(' ?', '').replace(
                        ' and ', '~').replace(' with ', '~').replace(
                            ' plus ', '~').strip()

    # Back out of the loop and everything joined together temporarily.
    temp_string = '~'.join(
        [x for x in chain.from_iterable(second_demension) if x != ''])

    # Using the Counter structure we add everthing into a dictionary.
    counter_dict = Counter(temp_string.split('~'))

    # Finally return everything in a sorted by name dicionary.
    return {k: v for (k, v) in sorted(
        zip(counter_dict.keys(), counter_dict.values()))}


# print(jam('data/jam.txt'))
