# https://www.hackerrank.com/contests/hackerrank-hiring-contest/challenges/winning-lottery-ticket

# Author:  Rohit Hegde - hegde.rohit7@gmail.com (https://www.github.com/rohegde7)
# status: Test cases passed, but timeout error (complexity is O(n-square)...try reducing it)

number_tickets = int(input())

list_sublist = [0,1,2,3,4,5,6,7,8,9]
list_tickets = []
counter = 0

for i in range(number_tickets):
    list_tickets.append(input().strip())

#print(list_tickets)

for i in range(number_tickets-1):
    for j in range(i+1, number_tickets):
        comb = list_tickets[i] + list_tickets[j]
        superset = list(map(int, list(comb)))
        #print("superset is:", superset)


        flag = 1
        for k in list_sublist:
            if k not in superset:
                flag = 0
                
        if flag == 1:
            counter += 1

print(counter)