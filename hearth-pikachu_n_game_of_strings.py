# Author: https://www.github.com/rohegde7 (Rohit Hegde - hegde.rohit7@gmail.com)

# https://www.hackerearth.com/challenge/competitive/august-easy-18/algorithm/pikachu-and-the-game-of-strings-1-8c22a8ce/

# status: Success (20/20 test cases passed)

'''
( Problem A ) Pikachu and the Game of Strings
Max. Marks: 100

Pikachu has recently learnt a new move 
. He knows he can work hard and convert it into a stronger move . Both the moves  and

 contain the same number of letters.

In a single day, Pikachu can increase any letter of move
 by one, that is, in a single day, he can convert letter to , to , to and so on. He can also convert letter to letter

. 

Pikachu just realized he also has a hidden ability. It can help him increase any letter of move
 by ,  that is, in a single day, he can convert letter to letter , into , into , into

and so on.  

Now Pikachu wants to know the minimum number of days in which he can convert the move
into move ?

SAMPLE INPUT
4
ABCT
PBDI

SAMPLE OUTPUT
7

'''
num_letters = int(input()) #not needed here as we use len() of python3

list_ip_string = list(input())
list_op_string = list(input())
#print(list_string)

no_days = 0

for i in range(len(list_ip_string)):

    diff = (ord(list_op_string[i]) - ord(list_ip_string[i]))    #to check how many characters we need to move
    if diff >=0:
        diff = diff%97
    else:
        diff = abs(diff)%97 #abs() is for some problem that python has when we take modulus of a -ve number
        '''diff gives the distance between 2 letters but we can only move forward
            So if I have to go from Z to Y, I have to goto Z-A-B-C....Y. Hence the next line: '''
        diff = 26-diff

    #print(diff)

    '''As we can move either 13 hops or 1 hop at a time, we'll 1st take as many as 13 hops;
        and when we no longer can take 13 hops we start taking 1 hop at a time;
        So when we take one '13 hops' it takes 1 day, also when we take one '1 hop' it takes 1 day'''

    while diff>=13:
        diff = diff-13
        no_days = no_days+1

    no_days = no_days+diff  #these are the number of '1 hops' we need to take as we no longer can take '13 hops'

print(no_days)

