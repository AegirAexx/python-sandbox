""" Competition in SC-T-308-PRLA. Writing the fewest characters. """


""" A string contains balanced parentheses if it contains the same number
of open and closed parentheses and for every open parentheses, there
appears a closed parentheses, to the right of it, in the string.

Write a function balanced that takes a string containing only parentheses.
The function returns True if the parentheses are balanced; else False."""

# >>> balanced('(()())()')
# True
# >>> balanced('(())())()')
# False
# print(balanced('(()())()'))
# print(balanced('(())())()'))
# print(balanced(")(')(',"))
# print(balanced("('',)"))


# from collections import Counter


# def balanced(s):
#     c = Counter([x for x in s if x == '(' or x == ')'])
#     if c['('] == c[')'] and s.rfind(r"(") < s.rfind(r")"):
#         return True
#     return False

def balanced(s):
    L = 0
    R = 0
    li = list(s)
    for x in li:
        if R > L:
            return False
        elif x == '(':
            L += 1
        elif x == ')':
            R += 1
    return L == R


# print(balanced('(()())()'))  # >> True
# print(balanced('(())())()'))  # >> False
# print(balanced(")(')(',"))  # >> False
# print(balanced("('',)"))  # >> True
# print(balanced('(())(()))(()'))  # >> False


"""A palindrome is a number that is read the same from left to right and
right to left. So, for example, 1331 is a palindrome but 1337 is not.

Whether a number is a palindrome depeonds on the system used to represent
the number. So for example, then number 73 is not a palindrome in base 10,
but since 73 = 1001001(2), we have that 73 is a palindrome in base 2.

Write a function palindrome that takes two integers 1 ≤ n ≤ 10^14 and
2 ≤ b ≤ 10^6 as parameters. The function returns True if n is a palindrome
in base b; False otherwise."""

# >>> palindrome(1331, 10)
# True
# >>> palindrome(73, 2)
# True
# >>> palindrome(1337, 10)
# False


def palindrome(a, b):
    pass


""" Programmers often need to write HTML code, which often consists of a
lot of repetition (like typing <tag>...</tag> a million times).
As programmers are usually pretty lazy and don't want to repeat this over
and over again, someone found a solution to this problem.

The solution consists of a small language to describe the structure of
HTML elements, which is then expanded into regular HTML. We will only
consider a subset of this language.

As an example, the string:

html>head+body>div+div+p>ul>li*3>a

is expanded into the string:

<html>
    <head>
    </head>
    <body>
        <div></div>
        <div></div>
        <p>
            <ul>
                <li><a></a></li>
                <li><a></a></li>
                <li><a></a></li>
            </ul>
        </p>
    </body>
</html>

In the language there are three special symbols:

    - The > symbol, which indicates that the rest of the HTML structure is
    nested inside the previous element.

    - The + symbol, which indicates that the rest of the HTML structure is
    adjacent to (a sibling of) the previous element.

    - The * symbol, which indicates that the previous element, and all its
    substructure, is repeated the specified amount of times (this symbol
    is always followed by an integer specifying the amount).

Write a function zen_expand(code) that takes as a parameter a single
string, which contains HTML structure encoded in the language described
above. The function should return a string which contains the expanded
HTML structure. Note that all whitespace is ignored, so pretty formatting
is not necessary (but still a fun challenge)."""

# >>> zen_expand("a+div+p*3")
# "<a></a><div></div><p></p><p></p><p></p>"
# >>> zen_expand("dd")
# "<dd></dd>"
# >>> zen_expand("table>tr*3>td*2")
# "<table><tr><td></td><td></td></tr><tr><td></td><td></td></tr>
# <tr><td></td><td></td></tr></table>"


def zen_expand(s):
    pass


""" In this problem, your task is to write a function all_palindromes that
takes a single parameter, a path to a file containing a list of words,
each word on a separate line. The function returns a list of all
palindromes that can be formed using exactly two words from the list of words.
When determining whether a pair of words is a palindrome we ignore both
casing and apostrophes.

The following word-pairs are, e.g., palindromes.

Dia's aid
A toyota
air aria
devil's lived
DNA's Sand

Your solution is tested on different sized files, namely:

small_words.txt,
med_words.txt,
big_words.txt,
special_words.txt.

Note that the largest file contains 200.000 words, so a naive approach
(a O(n2) solution) will not be fast enough to pass all tests."""

# >>> all_palindromes('/path/to/small_words.txt')
# ['Alala Alala', 'Mbm Mbm', 'Ono Ono', "Passe's sap", "Selz Azle's", 'xix xix']


def all_palindromes(s):
    pass


""" Your friend has recently acquired a large number of hamsters, through
means best left unsaid, and a 100 meter long wooden plank. Being extremely
bored, he decide to do some experiments (humane, of course) on his newly
obtained hamsters. He lays out his wooden plank, horizontally, and places a
number of hamsters randomly on the plank. He also orients the hamsters
randomly, so they're either facing the left or the right end of the plank.

After he has placed the hamsters on the plank, he blows a whistle and all the
hamsters start walking at the speed of 1 cm per second in the direction
they're facing. The plank is only wide enough to fit one hamster, so when two
hamsters meet, they both turn around on the spot and start walking in the
opposite direction. When the hamsters reach either end of the pole they
immediately fall off (and are, of course, not hurt by that).

Your friend did many experiments with his hamsters, and took careful notes of
them all. He, however, neglected to note the orientation of the hamsters, so
he asks for your help. He wants to know the least and the greatest amount of
time it could have taken all hamsters to clear the plank.

Your task is to write a function hamsters which takes a list of integers as a
parameter, each integer between 0 and 10000 (inclusive), in no particular
order. Each integer denotes a placement of a hamster on the plank, measured
in centimeters from the left end of the plank. The function returns a tuple
containing two integers, the least and greatest amount of time it could have
taken all hamsters to clear the plank, respectively. """

# >>> hamsters([100, 900])
# (900, 9900)


# from random import randrange


def hamsters(L):
    # If the list has only one number in it.
    if len(L) < 2:
        if L[0] > 5000:
            return tuple((10000 - L[0], L[0]))
        else:
            return tuple((L[0], 10000 - L[0]))

    # Fake input
    # L = [randrange(10001) for x in range(5)]

    # Generate List and iterable range
    sorted_list = sorted(L)
    length_iter = range(len(sorted_list))

    # Generate dictionaries to look up values - orginal and from 0k, 5k and 10k
    dict_list = {k: v for (k, v) in zip(length_iter, sorted_list)}
    dict_0k = {k: v for (k, v) in zip(sorted_list, length_iter)}
    dict_5k = {k: v for (k, v) in zip(
        [abs(x - 5000) for x in sorted_list], length_iter)}
    dict_10k = {k: v for (k, v) in zip(
        [10000 - x for x in sorted_list], length_iter)}

    # Find the least and the greatest time

    # Least - is the one closest to the center.
    least_value = min(dict_5k.keys())
    least_key = dict_5k.get(least_value)
    least_pre = dict_list.get(least_key)
    least = None
    if least_pre > 5000:
        least = 10000 - least_pre
    else:
        least = least_pre

    # Greatest - is the value of [0] from the start or the value of [-1] from the end.
    from_start = max(dict_0k.keys())
    from_end = max(dict_10k.keys())
    greatest = None
    if from_start > from_end:
        greatest = from_start
    else:
        greatest = from_end

    # return tuple((least, greatest))

    # Debug - Debug - Debug
    print('-' * 70)
    print('original input:', L)
    print('sorted list:', sorted_list)
    print('indexed dicionary:', dict_list)
    print('-' * 70)
    print('delta form start:', dict_0k)
    print('delta from center:', dict_5k)
    print('delta from end:', dict_10k)
    print('-' * 70)
    print('least - greatest:', tuple((least, greatest)))
    print('-' * 70)

    return tuple((least, greatest))


# print(hamsters([100, 900]))
# print(hamsters([10000]))
# print(hamsters([8486, 8145, 6002],))  # >>> (3998, 8486)
