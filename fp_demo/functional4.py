""" Playing around with REDUCE, MAP and Lambdas. """
from datetime import datetime
from functools import reduce  # Bring in reduce()
from pprint import pprint
import collections  # To bring in "Default Dictionary"
from scientist import scientists


def get_age(year_of_birth):
    """ Returns the age of the person. """
    return datetime.now().year - year_of_birth


AGE_LIST = tuple(map(lambda x: get_age(x.born), scientists))

pprint(AGE_LIST)

TOTAL_AGE = reduce(lambda acc, val: acc+val, AGE_LIST, 0)

# If used on a dictionary, a "key" can be set to reduce.
# reduce(lambda acc, val: acc + val['key'], dictionary, 0)

print('----------------')
pprint(TOTAL_AGE)


# Use reduce to create a dictionary that looks like this.
# {'math': [], 'physics': [], 'chemistry': [], 'astronomy': []}

def reducer(acc, val):
    """ Defining a reducer to create a Dictionary. """
    acc[val.field].append(val.name)
    return acc


SCIENTISTS_BY_FIELD_PREDEFINED_DICT = reduce(
    reducer,
    scientists,
    {'math': [], 'physics': [], 'chemistry': [], 'astronomy': []}
)

print('----------------')
pprint(SCIENTISTS_BY_FIELD_PREDEFINED_DICT)

SCIENTISTS_BY_FIELD_DEFAULT_DICT = reduce(
    reducer,
    scientists,
    collections.defaultdict(list)
)

print('----------------')
pprint(SCIENTISTS_BY_FIELD_DEFAULT_DICT)
