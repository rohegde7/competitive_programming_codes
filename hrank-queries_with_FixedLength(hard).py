# Author of the code: Rohit Hegde - hegde.rohit7@gmail.com (https://www.github.com/rohegde7)

# https://www.hackerrank.com/challenges/queries-with-fixed-length/problem
# status: working for 4/11 cases, Time complexity problem

n,q = map(int, input().split())    
#n = number of elements 
#q = number of d's; d is the number of elements in a group we need to make

list_elements = list(map(int, input().split()))
#print(list_elements)

for i in range(q):  #for collecting all the d's
    d = int(input())
    list_maximums = []  #stores max of each group ex: max(a0,a1,a3...)

    '''Next loop: need to travel only till the element from where 'd' number of elements are present 
       from the current element in order to make 'd' number of combinations 
       out of which we need to take out the maximum of those'''
    for j in list_elements[0:len(list_elements)+1-d]:
        start_point = list_elements.index(j)
        end_point = start_point + d
        list_maximums.append(max(list_elements[start_point:end_point]))

    print(min(list_maximums))
