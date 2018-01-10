# Author: https://www.github.com/rohegde7 (Rohit Hegde - hegde.rohit7@gmail.com)

# https://www.codechef.com/problems/MRO
# Problem Code: MRO
# status: Accepted, ET 0.05 secs

tests = int(input())

for i in range(tests):
    n = int(input())  #number of songs
    list_songs = list(map(int, input().split()))
    k = int(input())

    uncle_johny = list_songs[k-1]   #cause the question's indexing starts from 1

    list_songs.sort()

    print(list_songs.index(uncle_johny)+1)

