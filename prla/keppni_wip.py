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


def balanced(s):
    pass


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

is expanded into the string

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
casing and apostrophes. The following word-pairs are, e.g., palindromes.

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


def hamsters(l):
    pass
