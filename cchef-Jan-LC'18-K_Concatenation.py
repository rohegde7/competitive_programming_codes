# Author: https://www.github.com/rohegde7 (Rohit Hegde - hegde.rohit7@gmail.com)
# https://www.codechef.com/JAN18/problems/KCON
# Problem Code: KCON
# status: Test cases passed, rest only The Almighty knows

#def fun_sum(list_a, x):
    

test_cases = int(input())

for i in range(test_cases):
    size, k = map(int, input().split())

    list_a = list(map(int, input().split()))
    list_a *= k     #concatinating 'k' copies of the original array
    #list_a += [None]
    #print(list_a)

    max_sum = 0
    for x in range(len(list_a)):    #loop from 0 to full length of the list
        temp_sum = 0
        for y in range(x+1,len(list_a)+1):
            temp_sum = sum(list_a[x:y])
            #print("Temp sum is:" ,temp_sum)
            if temp_sum  > max_sum:
                max_sum = temp_sum

    print(max_sum)