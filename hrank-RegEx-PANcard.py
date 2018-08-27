import re
tests = int(input())

for i in range(tests):
    inp = input()
    
    x = re.findall(r'^[A-Z]{5}[0-9]{4}[A-Z]$', inp) #return a list of all the matches
    
    if not x:   #checking is the list is empty 
        print("NO")
    else:
        print("YES")