# https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem
# status: Done...19/19 test-cases passed!

itr = int(input())   #no. of input string sets

dct = { '}':'{', ']':'[', ')':'(' }     #defining the pairs as key:value

lst_opening = ['{', '[', '(']
lst_closing = ['}', ']', ')']

for x in range(itr):
    flag = 1    #the input is valid
    lst = []
    input_string = input()   #the string of the bracket set 
    for i in input_string:
        lst.append(i)
    #print(lst)

    lst_stack = []  #for storing the opening phases of brackets
    for i in lst:
        if i in lst_opening:
            lst_stack.append(i)     #pushing opening brackets into the list
        #if it is not in lst_opening then it has to be in lst_closing    
        elif len(lst_stack) == 0:   #if there is a closing bracket and no opening pair 
            flag = 0
        elif dct[i] == lst_stack[len(lst_stack)-1]: #check if the last element in the lst_stack is the opening pair of the current bracket
            lst_stack.pop()
        else:
            flag = 0    #no matching opening pair found for the current closing bracket
            
    if flag == 1 and len(lst_stack) == 0:   #len(lst_stack) is 0 if there is no opening bracket left.
        print("YES")
    else:
        print("NO")

            


                   
