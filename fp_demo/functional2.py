from pprint import pprint  # Makes the formating nice when printing tuples/lists
from scientist import scientists

# Using one lambda in filter.
winners = tuple(filter(lambda x: x.nobel is True, scientists))

print('---- Nobel Winners: -----')
pprint(winners)

print()
print()

# Using two lambdas in one filter.
physics_winners = tuple(filter(lambda p: p.field == 'physics' and p.nobel, scientists))

print('---- Physics Nobel Winners: ------')
pprint(physics_winners)

# Defining two filter functions
def physics_filter(x):
    return x.field == 'physics'

def nobel_filter(x):
    return x.nobel

print()
print()

print('------ with stacked filter functions ------')

# Stacking two filters together to make "building blocks" that can be used many times.
phy_win = tuple(filter(physics_filter, filter(nobel_filter, scientists)))

pprint(phy_win)

print()
print()

# List comprehension - Filter'ish
list_comp = tuple(x for x in scientists if x.nobel is True and x.field == 'chemistry')

print('------ with list comprehension ------')

pprint(list_comp)

