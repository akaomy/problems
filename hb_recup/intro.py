# 1. Write a function that takes in a list and prints each item in the list.
def print_each(lst):
    '''Print out each item in list'''
    for each in lst:
        print(each)


# print_each(['word1', 'word2', 'word3'])

# 2. Write a function that takes in a list of words. For each word,
# the function should print a tuple of (first_letter_of_word, word).

# input: [word1, word2, word3]
# output: (first_letter_of_word, word)

# questions:
# can words contain numbers, empty spaces and special chars?
# what if first letter is upper cased, do I need to put upper cased letter into tuple or all letters in tuple should be lowercased?
# do I need to check for words dublication?
# do I need to check for empty element string in a list?
# what if there are repeated first letters of each word?

# pseudocode:
# function print_tuple([salmon, telapia, som])
# print out tuple (slice first letter of a word, word)

# time complexity O(n)

def print_tuple(words_list):
    """Print out tuple of (first_letter_of_word, word) from given list of words"""

    try:
        for word in words_list:
            print((word[0], word))
    except IndexError:
        print('empty string value in a list')


# print_tuple(['salmon', '9salmon', '', ' telapia', 'som', 'som'])


# 3. Write a function that takes in a list of numbers. It should print
# every other number, starting with the number at index 0.

# input: list of numbers
# output: number on each line?

# what if list is empty?
# what if it has only one element?
# is it one dimentional list?
# can it contain other datatypes?
# should the output be sorted?

# pseudocode:
# funciton print_every_other([])
# loop through each element in the list
#   check if index of this element is divisible by 2 without reminder print it

# time complexity O(n)

def print_every_other(number_list):
    '''Print every other number in a given list'''

    for i, number in enumerate(number_list):
        if i % 2 == 0:
            print(number)

    # another solution
    # for number in number_list[::2]:
        # print(number)


# print_every_other([30, 1, 400, 2, 5, 0, 1])


# 4. Write a function that takes in a list and an item. It should return
# True if the list contains the item. Otherwise, return False.

# input: [] and an item
# output: boolean

# questions:
# what datatype has an items in the list and an item that we are searching for? is it important to know?

# pseudocode:
# if datatype is not important:
# function has_item(items_list, item)
# decalre var all_items = call set() on items_list
# check if item is in all_items return true

# time complexity O(n)

def has_item(items_list, item):
    '''Return True if item is in the list'''

    print(item in set(items_list))


# has_item(['salmon', '9salmon', ' telapia', 'som', 'som'], 'som')  # True
# has_item([30, 1, 400, 2, 5, 0, 1], 100)  # False


# 5. Write a function that takes in a string and returns the length
# of that string. You cannot use the len function.

# return a length of a string without using built in python function

# input: string
# output: number

# questions:
# is there a limitation to length of a string? how long or short it can be?
# what if there is an empty string?
# any characters in a string are counted not only letters?

# pseudocode:
# function string_length(str):
# create a counter variable
# loop through each char in a string
# each looping add +1 to counter
# once loop is done return the counter

# time complexity O(n)

def string_length(string_to_check):
    '''Return a length of a string without using built in python function'''

    counter = 0
    for char in string_to_check:
        counter = counter + 1

    print(counter)


# string_length('string')

# 6. Write a function that takes in a sentence as a string. The function should print the
# length of each word in the sentence. Your sentence will not contain any punctuation.

# return a length of each word in a given sentence

# input: string
# output: number

# questions:
# limitations on length of a string?
# is a number counted as a separate char?
# no punctuation, but what about white space?
# can I use build in len() function?

# pseudocode:
# function find_length_of_each_word(sentence):
# declare a var words_list = split sentence by whitespace
# for each word in call words_list
# call len()function on each word and return it

# time complexity O(n)

def find_length_of_each_word(sentence):
    '''return a length of each word in a given sentence'''

    words_list = sentence.split(' ')
    for word in words_list:
        print(len(word))


find_length_of_each_word('return a length of each word in a given sentence')

# 7. Write a function that takes in a list of numbers and returns the largest number in the list.
# You cannot use the max function.

# return largest number in a given list of nums

# input: []
# output: number

# questions:
# how long or short can be the list?
# what if list is empty?

# pseudocode:
# declare variable largest = 0
# loop thorugh each number in a list
# check if a number is more than largest
# if yes, assign new value of this num to largest
# return the largest once loop is done running

# time complexity O(n)


def largest_num(nums_list):
    '''Return largest number in a given list of nums'''

    largest = 0

    for num in nums_list:
        if largest < num:
            largest = num

    print(largest)


largest_num([30, 1, 00, 2, 5, 0, 1])
