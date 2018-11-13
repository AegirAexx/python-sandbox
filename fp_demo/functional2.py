""" Playing around with filter higher order function and lambda expresions. """
from pprint import pprint  # Nicer formatting when printing tuples/lists
from scientist import scientists

# Using one lambda in filter.
WINNERS = tuple(filter(lambda x: x.nobel is True, scientists))

print('---- Nobel Winners: -----')
pprint(WINNERS)

print()
print()

# Using two lambdas in one filter.
PHYSICS_WINNERS = tuple(
    filter(lambda p: p.field == 'physics' and p.nobel, scientists))

print('---- Physics Nobel Winners: ------')
pprint(PHYSICS_WINNERS)


def physics_filter(sci):
    """ Defining a filter function. """
    return sci.field == 'physics'


def nobel_filter(sci):
    """ Defining a filter function. """
    return sci.nobel


print()
print()

print('------ with stacked filter functions ------')

# Stacking filters together to make "blocks" that can be used many times.
PHY_WIN = tuple(filter(physics_filter, filter(nobel_filter, scientists)))

pprint(PHY_WIN)

print()
print()

# List comprehension - Filter'ish
LIST_COMP = tuple(
    x for x in scientists if x.nobel is True and x.field == 'chemistry')

print('------ with list comprehension ------')

pprint(LIST_COMP)
