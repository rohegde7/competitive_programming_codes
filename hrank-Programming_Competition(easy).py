# https://www.hackerrank.com/contests/hackerrank-hiring-contest/challenges/programming-competition

# Author:  Rohit Hegde - hegde.rohit7@gmail.com (https://www.github.com/rohegde7)

# status: Accepted :)

number_of_programmers = int(input())

list_names = []
list_diff = []
for i in range(number_of_programmers):
    name, d, j = input().split()
    d, j = map(int, [d,j])

    list_names.append(name)
    list_diff.append(j-d)

max_index = 0
#print(list_names, list_dec, list_jan)

for i in range(number_of_programmers):
    if list_diff[i] > list_diff[max_index]:
        max_index = i

print(list_names[max_index], list_diff[max_index])


""" Tried using dictionary but as dictionaries are not 'ordered', problem was arising

number_of_programmers = int(input())

dict_rank = {}
dict_total_solved = {}

for i in range(number_of_programmers):
    name, d, j = input().split()
    d,j = map(int, (d,j))

    dict_rank.update({ name: (j-d) })
    dict_total_solved.update({name: j})

for key,value in dict_rank.items():
    max_value = {key:value}
    max_k = key
    max_v = value
    break

for key,value in dict_rank.items():
    if value > max_v:
        max_value = {key:value}
        max_k = key
        max_v = value

for key,value in max_value.items():
    print(key, value) 
"""