from collections import Counter


def birthdays(string):
    st = string.split()
    dic = Counter(x[0:4] for x in st)
    return [tuple([k for k in st if k.startswith(x)])
            for x in [x for x in dic if dic[x] > 1]]
