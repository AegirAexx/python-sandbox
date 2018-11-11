from pprint import pprint
from scientist import scientists
from datetime import datetime

def age(x):
    return datetime.now().year - x

names_and_ages = tuple(map(lambda x: {'name': x.name, 'age': age(x.born)}, scientists))


pprint(names_and_ages)

print('---------------------------')

# String interpolation using format_map() & vars() | Also see formet()

#def ip_str(x):
#    age = datetime.now().year - x.born
#    message = '{x.name} is {age} years old.'
#    return message.format_map(vars())

def ip_str(x):
    data = '%s is %d years old' % (x.name, (datetime.now().year - x.born))
    return data

names_and_ages2 = tuple(map(lambda x: ip_str(x), scientists))

pprint(names_and_ages2)