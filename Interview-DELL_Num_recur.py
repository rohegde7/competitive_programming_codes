'''
We are given a fixed number(15) of names along with a fixed set of numbers(1-5).
We need to print out all the names in order and besides each name a number from the set in a loop manner.
Ex: Suppose we have 4 names A B C D E and 2 numbers [1,2]
    Output: 
        A 1
        B 2
        C 1
        D 2
        E 1
'''

no_names = 15   #given
numbers = [1,2,3,4]
list_names = []

for i in range(no_names):
    list_names += input().split()

number_indicator = 1
number_index = 0

for i in range(no_names):
    print(list_names[i], numbers[number_index])

    if number_index == 0:
        indicator = 1
    
    if number_index == 3:
        indicator = -1

    if indicator == 1:
        number_index += 1
    else:
        number_index += -1
