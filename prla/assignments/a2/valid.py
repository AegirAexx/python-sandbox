from datetime import date
from itertools import cycle, starmap
from operator import mul


def valid(number_string):
    """ See project description."""

    # Add the string version of the numbers to an array as actual numbers.
    numbers = [int(number) for number in number_string]

    # Make each number into it's own variable.
    # d[1&2] = day, m[1&2] = month, y[1&2] = year, r[1&2] = random,
    # c = checksum and m = century.
    d1, d2, m1, m2, y1, y2, r1, r2, c, m = numbers

    # Check conditions to filter out non-valid numbers.

    # If born in the 20th century.
    if m == 9:
        # Run the through datetime.date and catch the ValueError.
        try:
            date(1900 + 10 * y1 + y2, 10 * m1 + m2, 10 * d1 + d2)
        except ValueError:
            return False
    # If born in the 21st centrury.
    elif m == 0:
        # Run the through datetime.date and catch the ValueError.
        try:
            date(2000 + 10 * y1 + y2, 10 * m1 + m2, 10 * d1 + d2)
        except ValueError:
            return False
    # If the last digit is not a nine or a zero then it's not valid.
    else:
        return False

    # If the number passed the conditions above we try the checksum.
    # checksum = 11-((3*D1+2*D2+7*M1+6*M2+5*Y1+4*Y2+3*R1+2*R2)mod11)
    # The check is executed with some nice library tools but could
    # just as easily been done with the regular checksum formula.
    return c == (11 - sum(starmap(mul, zip(
        map(int, cycle('32765432')), numbers[0:8]))) % 11)


# print(valid('2096814019'))
# print('-' * 20)
# False
# print(valid('2006814019'))
# print('-' * 20)
# True
# print(valid('0212862149'))
# print('-' * 20)
# True
# print(valid('1803442379'))
# print('-' * 20)
# False
