# creates two variables
# reads from standard input
# computes the sum
# outputs the sum in the standart output

import timeit

input  = input().split() # ['...', '...', ...]
a = input[0] # type str
b = input[1] # type str
res = int(a)+int(b)

print(res) 
# how long code runs:
print(min(timeit.repeat(a+b))) # strings as input to timeint only



# what i learned here:
# use of timeint