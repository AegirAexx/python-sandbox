"""" Playing around with MAP higher order function and lambdas. """
from datetime import datetime
from pprint import pprint
from scientist import scientists

def age(yob):
    """ Accepts year of birth and returns the persons age. """
    return datetime.now().year - yob

NAMES_AND_AGES = tuple(
    map(lambda x: {'name': x.name, 'age': age(x.born)}, scientists))


pprint(NAMES_AND_AGES)

print('---------------------------')


def ip_str_1(sci):
    """String interpolation using format_map() & vars() | Also see format()."""
    sci_age = datetime.now().year - sci.born
    message = '{sci.name} is {sci_age} years old.'
    return message.format_map(vars())

def ip_str_2(sci):
    """String interpolation using format_map() & vars() | Also see format()."""
    data = '%s is %d years old' % (sci.name, (datetime.now().year - sci.born))
    return data

NAMES_AND_AGES2 = tuple(
    map(lambda x: ip_str_2(x), scientists))

pprint(NAMES_AND_AGES2)
