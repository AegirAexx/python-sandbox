""" Playing around with immutable data types and pprint. """
from pprint import pprint  # Prettier printing of lists
from scientist import Scientist

print(Scientist)

ADA = Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False)

print('--------------')
print(ADA.name)
print(ADA.field)
print(ADA.born)
print(ADA.nobel)
print('--------------')
pprint(ADA)
print('--------------')
print(ADA)
