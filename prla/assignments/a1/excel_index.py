def excel_index(column):
    return sum(26**i * (ord(x) - 64) for i, x in enumerate(reversed(column)))
