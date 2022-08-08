# TODO: determine runtime for each funciton:

def does_string_contain_letter(letter, string):
    """Determine whether a given letter is in a string."""

    return letter in string

# My answer: O(n)
# Correct answer:


def contain_letters_in_common(string1, string2):
    """Determine whether the two strings have any letters in common."""

    duplicates = []
    for letter in string1:
        if letter in string2:
            if letter not in duplicates:
                duplicates.append(letter)

    return len(duplicates) > 0

# My answer: O(n)
# Correct answer:


def letters_in_common(string1, string2):
    """Return a list of letters in common between two strings.
    If a letter appears more than once, the list should only contain the letter
    once.
    """

    duplicates = set()
    string2 = set(string2)
    for letter in string1:
        if letter in string2:
            duplicates.add(letter)

    return list(duplicates)

# My answer: O(n)
# Correct answer:


# more here (JS):
# function logUpTo(n) {
#     for (var i = 1; i <= n; i++) {
#         console.log(i);
#     }
# }

# Answer: O(n)


# function logAtMost10(n) {
#     for (var i = 1; i <= Math.min(n, 10); i++) {
#         console.log(i);
#     }
# }

# Answer: O(1)


# function logAtLeast10(n) {
#     for (var i = 1; i <= Math.max(n, 10); i++) {
#         console.log(i);
#     }
# }

# Answer: O(n)


# function onlyElementsAtEvenIndex(array) {
#     var newArray = Array(Math.ceil(array.length / 2));
#     for (var i = 0; i < array.length; i++) {
#         if (i % 2 === 0) {
#             newArray[i / 2] = array[i];
#         }
#     }
#     return newArray;
# }

# Answer: O(n)


# function subtotals(array) {
#     var subtotalArray = Array(array.length);
#     for (var i = 0; i < array.length; i++) {
#         var subtotal = 0;
#         for (var j = 0; j <= i; j++) {
#             subtotal += array[j];
#         }
#         subtotalArray[i] = subtotal;
#     }
#     return subtotalArray;
# }

# Answer: O(n^2)
