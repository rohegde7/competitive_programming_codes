# Author: https://www.github.com/rohegde7 (Rohit Hegde - hegde.rohit7@gmail.com)

# https://www.codechef.com/COOK97B/problems/BFTT
# Problem Code: BFTT

# status: Success :)

n_tests = int(input())

for i in range(n_tests):
    n = int(input())
    n1 = n

    count = 0
    while(count < 3):
        n1 = n1+1
        count = 0

        lst_n = [int(x) for x in str(n1)]

        for x in lst_n:
            if x == 3:
                count = count+1

        

    print(n1)

    
    