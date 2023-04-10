# goal is to implement a program that works in less than one 
# second even on huge datasets

# problem statement:
# given an array of integers
# find product of 2 largest numbers in the array


# questions:
# array has no subarrays?
# error messages if there are non integer items in the array?


# pseudocode:
# create max_product variable and assign it to 0
# go through each item in the array
# multiply each item in the array with each item in the array
# check if max_product is less than result of multiplication
# add the result of multiplication to max_product variable


input = input().split()
# translate each string item in the array to int
int_input = []
[int_input.append(int(item)) for item in input]



import time

start_time = time.time()
# brute force
# max_prod = 0
# for each in int_input:
#     for each2 in int_input:
#         if max_prod < each2 * each:
#             max_prod = (each * each2)
# print(max_prod)
# print("--- %s seconds ---" % (time.time() - start_time))
# for this input 
# 999999999999999999 999999999999999999 999999999999999999 999999999999999999 999999999999999999 999999999999999999 999999999999999999 999999999999999999 999999999999999999 999999999999999999 999999999999999999 999999999999999999 999999999999999999 999999999999999999 999999999999999999
# 3.981590270996094e-05 
# 4.363059997558594e-05
# 5.030632019042969e-05

# faster solution
# [do something here for each item in this array_list]
# [each2 for each2 in int_input for each in int_input]
# [[each for each in int_input] max_prod = (each * each2) for each2 in int_input if max_prod < each2 * each]

# step 1:
# [[print(each, each2) for each in int_input] for each2 in int_input]

# step 2
# max_prod = 0
# [[each*each2 for each in int_input] for each2 in int_input]

# step 3
max_prod = 0
res = [[max_prod:=(each*each2) for each in int_input if max_prod < (each * each2)] for each2 in int_input]
print(max_prod)
# step 4
# bug fix: max_prod is not correct
# e.g. if there are 1 2 3 in the array, result should be 6


# what i learned here:
# assignment operator in list comprehension => :=