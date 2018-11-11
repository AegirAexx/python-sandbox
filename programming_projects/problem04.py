''' Largest palindrome product
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.'''

def check_if_palindrome(string):
    start = str(string).lower()
    forward = list(start)
    backward = list(reversed(forward))
    end = ''.join(backward)
    return start == end

def find_highest_palindromic_number(number):
    highest = 0
    index_i = 10
    while(index_i < number):
        index_j = 1
        while(index_j < number):
            temp = index_i * index_j
            if check_if_palindrome(temp) and temp > highest:
                highest = temp
            index_j += 1
        index_i += 1
    return highest

print(find_highest_palindromic_number(1000))
