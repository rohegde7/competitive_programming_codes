'''
Given a number N, print reverse of number N.
Note: Do not print leading zeros in output.

For example N = 100 Reverse of N will be 1 not 001.

Input: Input contains a single integer N. Output: Print reverse of integer N.

Constraints: 1<=N<=10000
'''

number = input()    #storing the numeber in string format to iterate through it
len_number = len(number)
reverse_number = ""
flag = 1 #this will be used for avoiding leading zeros, 1 signifies that the 1st non-zero digit is not yet found


for i in range(len_number-1, -1, -1):   #iterate the string in reverse order
    if flag == 1 and int(number[i]) == 0:   #check for leading zero
        continue
    
    flag = 0    #confirms that we found 1st non-zero digit, now zeros are allowed
    reverse_number = reverse_number + number[i]

print(reverse_number)