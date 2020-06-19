'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # counting the occurences of th in the string. there are no spaces in the string.
    # are we recursively checking the next one?

    # set necessary variables

    word_length = len(word)

    sub = "th"

    sub_length = len(sub)

    # check to make sure that the word is long enough to contain two characters

    if sub_length > word_length:

        return 0

    # base case is we find a pair of indexes with the values t and h side by side
    # and we return 1
    # need to keep recursing

    if word[0:sub_length] == sub:

        return count_th(word[sub_length - 1:]) + 1

    else:
        # recurse some more

        return count_th(word[sub_length - 1:])

        # check to make sure pointer won't go out of bounds and stops at the end len(word)-1

        # increment window

        # call function
