# https://www.codechef.com/problems/COINS
# Problem code: COINS
# status: Time limit exceeded, but sample test cases passed.

def fun_div(num):
    n1 = int(num/2)
    n2 = int(num/3)
    n3 = int(num/4)

    list_temp = [num]
    if (n1+n2+n3) <= num:
        return list_temp
    else:
        return fun_div(n1) + fun_div(n2) + fun_div(n3)

while True:
    try:
        n = int(input())    #the integer on the given coin
        
        lst = [n]
        lst = fun_div(n)    #this funct will divide the integer into sets of n/2, n/3, n/4

        print(sum(lst))
    except:
        break