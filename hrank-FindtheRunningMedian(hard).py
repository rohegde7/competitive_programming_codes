# Author of the code: Rohit Hegde - hegde.rohit7@gmail.com (https://www.github.com/rohegde7)

# https://www.hackerrank.com/challenges/find-the-running-median/problem
# status: 3/9 cases passed, TIME complexity prob

n = int(input())    #number of elements to take


list_elements = []  #contains all the running numbers whose median needs to be calculated
for i in range(n):
    list_elements.append(int(input()))
    #list_elements.sort()
    list_elements = sorted(list_elements)
    #both sorting methods gave almost the same time complexity, so this is not the problem right now
    #print("List: ", list_elements)


    leng = len(list_elements)
    if leng%2 == 1:   #there are odd number of elements
        median = list_elements[int(leng/2)]   #will print the middle element
        print(round(float(median),1))
        continue    #will work without this but just thought why check for else when if is done and dusted
    else:   #even number of elements are present
        median = (list_elements[int(leng/2-1)]+list_elements[int(leng/2)]) / 2
        print(round(median,1))