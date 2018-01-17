# Author: https://www.github.com/rohegde7 (Rohit Hegde - hegde.rohit7@gmail.com)
# https://www.codechef.com/JAN18/problems/MAXSC
# Problem Code: MAXSC
# status: sub-task1: 1/2 passed, sub-task2: 1/4 passed

"""method:
        Sort all the rows of the matrix in decending order.
        Assign the max, i.e. 1st element(as it is sorted) of last row as the sum(max_sum).
        We then start from 2nd last row, crawl up the rows and find the max element in each row which is smaller than the max element chosen in the row below it.
"""

t = int(input())

for i in range(t):
    n = int(input())

    #taking matrix input
    list_matrix = []
    for m in range(n):
        list_matrix.append(list(map(int, input().split())))
    
    for temp in range(len(list_matrix)):
        list_matrix[temp] = sorted(list_matrix[temp], reverse = True)

    #print("The sorted matrix:\n", list_matrix, "\n")

    max_sum = list_matrix[n-1][0]   #stores the final sum that needs to be calculated
    cur_max = list_matrix[n-1][0]   #stores the max element in the below row with which to compare
    for x in range(n-2,-1,-1):
        flag = 0
        for y in list_matrix[x]:
            if y < cur_max:
                max_sum += y
                cur_max = y
                flag = 1    #denotes that an element smaller than the cur_max was found
                break
        
        if flag == 0:
            print("-1")
            exit()

    print (max_sum)