""" Assignment two in the Cteate a Blockchain with Python course. """


NAMES = list(('Aegir', 'Rosa', 'Hafrun', 'Hronn', 'Oli', 'Thorvaldur', 'Ada'))


def names_is_empty():
    """ Returns if the NAMES list is empty or not. """
    return len(NAMES) < 1


print('Names longer than 5 - contain \'n\' or \'N\'?')

for name in NAMES:
    is_n = False
    if len(name) > 5:
        temp = name.lower()
        for letter in temp:
            if letter == 'n':
                is_n = True
        if is_n:
            print('YES - %s' % name)
        else:
            print('NO - %s' % name)

print('-' * 40)

while not names_is_empty():
    print(NAMES.pop())
