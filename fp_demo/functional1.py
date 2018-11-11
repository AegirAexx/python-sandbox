from pprint import pprint # Prettier printing of lists
from scientist import Scientist

print(Scientist)

ada = Scientist(name = 'Ada Lovelace', field = 'math', born = 1815, nobel = False)

print('--------------')
print(ada.name)
print(ada.field)
print(ada.born)
print(ada.nobel)
print('--------------')
pprint(ada)
print('--------------')
print(ada)