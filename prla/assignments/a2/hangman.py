import re


def constructor(guessed, dashes):
    """ Returns the partially constucted string for the regular
    expression string."""
    # By placing all the guessed letters and the number of dashes seen
    # into the string. The expresion excludes capital letters, all letters
    # not in the English alphabet and apostrophes.
    return '[^\'A-Z\x80-\xFF' + guessed + ']{' + str(dashes) + '}'


def hangman(file_name, state, guessed):
    """ See project description."""
    # Dynamically construct a regular expression to match possibilities
    # against a dictionary of words.

    # First append to the list, a caret.
    reg_ex_lis = ['^']
    # A variable to track the number of consecutive dashes in the string.
    dashes = 0
    # Loop through the state string to count letters and dashes.
    for index in state:
        # Each iteration we test two conditions.

        # Check if the index is a dash and if dash count is greater than 0.
        if dashes != 0 and index != '-':
            # Call the scaffold constructor.
            reg_ex_lis.append(constructor(guessed, dashes))

        # Check if the current index is a dash of not.
        if index != '-':
            # If it is not a dash, append the the letter and zero the
            # dash counter.
            reg_ex_lis.append(index)
            dashes = 0
        else:
            # If it is a dash, add one to the counter.
            dashes += 1

    # Out of the loop, we check if the dash counter is greater than zero.
    if dashes != 0:
        # If true, we append the dash count to the end of the string list.
        reg_ex_lis.append(constructor(guessed, dashes))
    # Last we close the string with the dollar sign.
    reg_ex_lis.append('$')
    # With everything ready we run the constructed string list through
    # the regular expresion compiler.
    reg_ex = re.compile(r''.join(reg_ex_lis))

    # Last step is to run the regular expresion against each word in the
    # dictionary file.

    # An empty array to return the words matched.
    results = []
    # Loop through the file given.
    with open(file_name) as _file:
        for line in _file:
            # Strip all the whitespace pollution.
            line = line.strip()
            # Look for a match with re.search
            match = re.search(reg_ex, line)
            # If it turns out to be a match...
            if match is not None:
                # ...append it to the list
                results.append(line)
    # Return the words that matched the state given.
    return results


print(hangman('./data/all_words.txt', '-e--e-ti--', 'aeiostuvx'))
