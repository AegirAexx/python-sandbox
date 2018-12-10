from itertools import permutations


def countdown(a, b):
    i = 4
    lis = []
    while i < 10:
        temp = list(permutations(b, i))
        for x in temp:
            lis.append(''.join(x))
        i += 1
    ready = set(lis)
    result = []
    with open(a) as f:
        for line in f:
            line = line.strip()
            if line in ready:
                result.append(line)
    return result


print(countdown('./data/all_words_no_short.txt', 'pythonxyz'))
# ['hont', 'hypo', 'hypt', 'onyx', 'phony', 'phyton', 'pnxt', 'pnyx', 'pont',
# 'ponty', 'pony', 'poxy', 'poynt', 'pynot', 'pyot', 'python', 'thon', 'tony',
# 'toph', 'typhon', 'typo', 'typy', 'tyyn', 'yont']
