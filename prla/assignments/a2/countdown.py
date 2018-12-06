# from itertools import product
from pprint import pprint
import re


def countdown(a, b):
    reg_string = re.compile('^(?:([' + b + '])(?!.{1}\1))+$')
    results = []
    with open(a) as f:
        for line in f:
            line = line.strip()
            search = re.search(reg_string, line)
            if search is not None and 9 >= len(line) > 3:
                results.append(line)
    return results


print(countdown('./data/all_words_no_short.txt', 'pythonxyz'))
# ['hont', 'hypo', 'hypt', 'onyx', 'phony', 'phyton', 'pnxt', 'pnyx', 'pont',
# 'ponty', 'pony', 'poxy', 'poynt', 'pynot', 'pyot', 'python', 'thon', 'tony',
# 'toph', 'typhon', 'typo', 'typy', 'tyyn', 'yont']
