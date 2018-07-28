'''here we take a ready-made text file for our reference
    and ask user for the word to be searched'''

read_file = open('deepcompute.txt', 'r') #opening to read only

list_words = list(read_file.read().split())
#print(list_words)
word_search = input("Enter the word to search\n").lower()

#we'll convert all the words in lower case 1st
for word in list_words:
    list_words[list_words.index(word)] = word.lower()

occur_num = list_words.count(word_search)

print("The word appears ", occur_num, " times in the file.")
