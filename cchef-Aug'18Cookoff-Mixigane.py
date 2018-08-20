# Author: https://www.github.com/rohegde7 (Rohit Hegde - hegde.rohit7@gmail.com)

# https://www.codechef.com/COOK97B/problems/MIXGA
# Problem Code: MIXGA

# status: Success :)

n_tests = int(input())

for i in range(n_tests):
    n, k = map(int, input().split())
    
    lst_num = list(map(int, input().split()))

    total = 0
    for i in range(len(lst_num)):
        sum1 = abs(total+lst_num[i])
        sum2 = abs(total-lst_num[i])

        if i%2 == 0:
            if sum1 > sum2:
                total = sum1
            else:
                total = sum2

        else:
            if sum1 > sum2:
                total = sum2
            else:
                total = sum1

    if abs(total) >= k:
        print("1")
    else:
        print("2") 
        

        
