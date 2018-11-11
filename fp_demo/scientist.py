from collections import namedtuple

# Use Tuples over lists because lists are mutable while tuples are not.
# Named Tuples class - immutable
Scientist = namedtuple('Scientist', [
  'name',
  'field',
  'born',
  'nobel',
])

# Using tuples rather than list - immutable
# A tuple of NamedTuples.
scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)
