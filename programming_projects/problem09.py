""" Special Pythagorean triplet
    A Pythagorean triplet is a set of three natural numbers,
    a < b < c, for which, a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc."""

# Brute force - Counld not think of anything else that was more elegant.


def find_pythagorean_triplet():
    for c in range(1000, 1, -1):
        for b in range(1000, 1, -1):
            for a in range(1000, 1, -1):
                if a < b < c:
                    if a + b + c == 1000:
                        if a**2 + b**2 == c**2:
                            return dict({
                                'a': a,
                                'b': b,
                                'c': c,
                                'Their product': a*b*c
                            })
    return 'It didn\'t work'


print(find_pythagorean_triplet())
