from collections import Counter


def duplicates(lis):
    return list(Counter(lis) - Counter(set(lis)))
