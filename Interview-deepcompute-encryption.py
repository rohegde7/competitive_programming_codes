'''
Encrypt the characters by assigning it to the next character in the list
'''

input_string = input("Enter message to encrypt\n")
input_string = list(input_string)

list_alphabets_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list_alphabets_upper = []   #all upper case alphabets

#to include all upper case characters:
for i in range(26):
    list_alphabets_upper.append(list_alphabets_lower[i].upper())

for index in range(len(input_string)):
    char = input_string[index]
    if char in list_alphabets_lower:  #we need to encrypt only characters
        #encrypted_char = chr(ord(char)+1)   #encrypting to the next alphabet
        encrypted_char = list_alphabets_lower[(list_alphabets_lower.index(char)+1)%len(list_alphabets_lower)]

        input_string[index] = encrypted_char

    if char in list_alphabets_upper:  #we need to encrypt only characters
        #encrypted_char = chr(ord(char)+1)   #encrypting to the next alphabet
        encrypted_char = list_alphabets_upper[(list_alphabets_upper.index(char)+1)%len(list_alphabets_upper)]

        input_string[index] = encrypted_char


encrypted_string = "".join(input_string)

print(encrypted_string)