def is_palindrome(s):
    f = s.replace('\'', '').replace(' ', '').lower()
    t = list(reversed(f))
    b = ''.join(t)
    return f == b


def all_palindromes(s):
    with open(s) as f:
        word = f.read().splitlines()
    return [w for w in word if is_palindrome(w)]


# print(is_palindrome('Alala Alala'))
# print(is_palindrome('Mbm Mbm'))
# print(is_palindrome('Zeuglodontia\'s'))
# print(is_palindrome('Taco Cat'))

# print(all_palindromes('aegir.txt'))
# print(all_palindromes('small_words.txt'))
# print(all_palindromes('med_words.txt'))
# print(all_palindromes('big_words.txt'))
# print(all_palindromes('special_words.txt'))
# ['Alala Alala', 'Mbm Mbm', 'Ono Ono', "Passe's sap",
# "Selz Azle's", 'xix xix']
