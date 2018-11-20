""" Assignment 1 in the Udemy Build a Blockchain with Python course. """


NAME = 'Aegir'
AGE = 37


def get_input():
    """ Gets input from the user a sets them globally. """
    global NAME
    NAME = input('Please enter a name: ')
    global AGE
    AGE = int(input('Please enter an age: '))


def calculate_decades(age):
    """ Accepts an age and returns the decades
    that the person has been alive."""
    return age // 10


def printer(first, last):
    """ Accepts any two variables and prints them out. """
    print('\nThis is the first argument:"{first}" '
          'and this is the last argument:"{last}"'
          .format(first=first, last=last))


# Prints the current global variables.
print('Your name is {n} and you are {a} years old\n'.format(n=NAME, a=AGE))

# Gets input from the user and sets them globally.
get_input()

# Prints out the new information set in the global variables.
print('\nHi {n}, you\'ve been alive for {d} decades'
      .format(n=NAME, d=calculate_decades(AGE)))

# Prints out any two variables passed as arguments.
printer('Python', 'Blockchain')
