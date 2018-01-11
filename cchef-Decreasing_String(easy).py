# Author of the code: Rohit Hegde - hegde.rohit7@gmail.com (https://www.github.com/rohegde7)

# https://www.codechef.com/problems/DECSTR
# Problem Code: DECSTR
# status: Accepted, ET 0.01 secs

tests = int(input())

for i in range(tests):
    k = int(input())

    full_string = 'zyxwvutsrqponmlkjihgfedcba'
    final_string = ''
    repeat = int(k/25)
    remainder = k%25
    #print("Repeat:", repeat)
    #print("Remainder:", remainder)

    for x in range(remainder,-1,-1):
            if remainder == 0:
                continue

            final_string += chr((x%25)+97)

    for y in range(repeat):
        final_string += full_string

    print(final_string) 
