# https://www.codechef.com/JAN18/problems/RECTANGL
# code: RECTANGL
# status: ACCEPTED

t = int(input())

for i in range(t):
    lst_sides = list(map(int, input().split()))
    lst_sides.sort()

    if lst_sides[0] == lst_sides[1] and lst_sides[2] == lst_sides[3]:
        print("YES")
    else:
        print("NO")
