from operator import mul


def list_product(*args):
    return list(map(mul, *args))
