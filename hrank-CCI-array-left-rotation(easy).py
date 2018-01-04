#https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
#status: ACCEPTED :)

n,lr = map(int, input().split())
lst = list(map(int, input().split()))

for i in range(lr):
    p = lst.pop(0)
    lst.append(p)

print(*lst)

