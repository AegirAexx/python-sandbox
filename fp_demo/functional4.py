
import collections # To bring in "Default Dictionary"
from functools import reduce # Bring in reduce()
from scientist import scientists
from pprint import pprint
from datetime import datetime


def get_age(year_of_birth):
    return datetime.now().year - year_of_birth

age_list = tuple(map(lambda x: get_age(x.born), scientists))

pprint(age_list)

total_age = reduce(lambda acc, val: acc+val, age_list, 0)

# If used on a dictionary, a "key" can be set to reduce.
# reduce(lambda acc, val: acc + val['key'], dictionary, 0)

print('----------------')
pprint(total_age)


# Use reduce to create a dictionary that looks like this from the list of scientists
# {'math': [], 'physics': [], 'chemistry': [], 'astronomy': []}

def reducer(acc, val):
    acc[val.field].append(val.name)
    return acc

scientists_by_field_predefined_dict = reduce(
    reducer,
    scientists,
    {'math': [], 'physics': [], 'chemistry': [], 'astronomy': []}
)

print('----------------')
pprint(scientists_by_field_predefined_dict)

scientists_by_field_default_dict = reduce(
    reducer,
    scientists,
    collections.defaultdict(list)
)

print('----------------')
pprint(scientists_by_field_default_dict)
