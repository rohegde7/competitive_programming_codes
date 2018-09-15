'''
Given an array of numbers, arrange them in a way that yields the largest value. 
For example, if the given numbers are {54, 546, 548, 60}, the arrangement 6054854654 gives the largest value.

Input: First line contains an integer N, Next line contains N integers separated by space.

Output: Print the maximum number that can be obtained by using given numbers.

Constraints: 1<=N<=1000 1<=Number<=1000000
'''

n = int(input("Enter the number of elements:\n"))

list_numbers = list(map(int, input("Enter the numbers separated by space:\n").split()))
length = len(list_numbers)

for i in range(0, length-1):
    for j in range(i+1, length):
        combi1 = int(str(list_numbers[i]) + str(list_numbers[j]))
        combi2 = int(str(list_numbers[j]) + str(list_numbers[i]))

        if combi1 < combi2:
            list_numbers[i], list_numbers[j] = list_numbers[j], list_numbers[i]

largest_number_str = ""
for num in list_numbers:
    largest_number_str = largest_number_str + str(num)

print(largest_number_str)