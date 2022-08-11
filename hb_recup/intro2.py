# task: is to create a funciton that would takes in a list words
# and for each word it would return a tuple of first word letter and the word itself

# input []
# output ()

# tests:
# input: ' ' output: None
# input: special char in string output: return None
# input: numbers output: return None

# pseudocode
# go through each item in the fiven list
# we would create a tuple for each of it
# return tuple with first letter of a word and a word itself

# code

def tupleWords(words_list):

    for word in words_list:

        if word == ' ':
            print(None)
            continue

        if word.isalpha() == False:
            print(None)
            continue

        print((word[0], word))


# testing
# tupleWords(['return', 'tuple', 'with', 'first', 'letter'])
tupleWords(['123', 'tuple', ' ', 'first', 'letter'])
