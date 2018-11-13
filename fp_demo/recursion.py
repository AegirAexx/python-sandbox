""" Playing around with simple recursion. """


def rec(number):
    """ Recursive function that prints every step of the way for easy tracking.
    This function does not do anything but helped me figure things out in
    Python. One of my first ever functions in the programming language. """
    result = '- Result in the beginning -'
    if number < 0:
        result = 0
    else:
        print('Before(number): ', number)
        print('Before(result): ', result)
        result = number + rec(number - 1)
        print('After(number): ', number)
        print('After(result): ', result)
    return result


print('\n\nRecursion Example Results')
rec(6)
