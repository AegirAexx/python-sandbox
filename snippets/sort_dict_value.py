''' A code snippet from Dan Bader's e-mail blast.
    [https://dbader.org/blog/] '''
# How to sort a Python dict by value
# (== get a representation sorted by value)
import operator

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

sorted_dict_1 = sorted(xs.items(), key=operator.itemgetter(1))
# print(sorted_dict_1) ==>> [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:

sorted_dict_2 = sorted(xs.items(), key=lambda x: x[1])
# print(sorted_dict_2) ==>> [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
