from itertools import count


def flatten(lis):
    d = dict(zip(sorted(lis), count()))
    return [d.get(x) for x in lis]
