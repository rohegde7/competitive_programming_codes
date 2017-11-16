#ACCEPTED :)
#https://www.hackerrank.com/contests/w35/challenges/lucky-purchase

def price_check(v):
    
    list_digits = map(int, v)
    #print list_digits
    four = 0
    seven = 0

    for i in list_digits:
        if i == 4:
            four += 1
        elif i == 7:
            seven += 1
        else:
            return -1

    #print four, seven
    if four == seven:
        return int(v)
    else:
        return -1
            

no_books = input()
price = -2
dict_books = {}

for i in range(no_books):
    
    key,val = raw_input().split()
    dict_books[key] = val
    #print dict_books

    temp=price_check(val)
    #print temp
    if (temp > -1) and (price != -1):
        price = temp
    
    #print price

if str(price) in dict_books.values():
    for key,value in dict_books.iteritems():
        if value==str(price):
            print key
else:
    print -1

    

