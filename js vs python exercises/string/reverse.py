""" exercises from easiest to hardest to practice string manipulation """

# problem 1
# v1
def reverse_string(given_string):
    """ reversing a given string: long way"""
    if len(given_string) == 0:
        return

    new_string = ""
    for each in given_string:
        new_string = each + new_string

    print(new_string)

reverse_string('abcde')

# v2
# short way
print('abcde'[::-1])


# v3
def recursively_reverse_string(given_string):
    """ recursively trying to reverce string and print it out """
    if len(given_string) <= 1:
        return given_string
    else:
        return given_string[-1] + recursively_reverse_string(given_string[:-1])

ST = 'abcde'
recst = recursively_reverse_string(ST)
print(recst)

