'''
You are on your way to find the gifts. All the gifts lie in your path in a straight line at prime numbers and your house is at 0.
Given your current position find the closest gift to your position, and calculate the distance between your current position and gift and tell the distance.

Ex: For input 0, the output is 2 For number = 11, the output should be 0 For number = 2000000000, the output should be 11 For number = 1800000001, the output should be 10
'''

number = int(input())

if number >= 2:
    temp_num = number
    while(True):
        flag = 1
        for i in range(2,temp_num):
            if temp_num%i == 0:
                flag = 0
                break

        if flag == 1:
            print(temp_num-number) #the distance
            break
        
        temp_num = temp_num + 1


elif number < 0:
    print("Invalid")
    exit()

elif number == 1:
    print("1") #as next prime number is 2, so the distance is 1

elif number == 0:
    print("0")