#https://www.hackerrank.com/challenges/largest-rectangle/problem
#partial test case execution due to timeout
#import whatever

n = input() #number of buildings

build = raw_input().split()
build = map(int, build)

#print build

area = 0
for i in range(n):
    for j in range(i,n):
        count=1
        #temp_area = min(build[i:j+1])*(count)...count not working
        temp_area = min(build[i:j+1])*(j-i+1)
        count = count+1
    
        if temp_area > area:
            area = temp_area

        #print "Area after going from ", i+1, " to ", j+1, " is: ", area

print area

#input: >>5 >>1 2 3 4 5 

