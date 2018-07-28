input_string = input("Enter message to encrypt\n")
input_string = list(input_string)

list_alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#Mannul typing is boring so code it (to include all upper case characters):
for i in range(26):
    list_alphabets.append(list_alphabets[i].upper())

#now list_alphabets contains all lower and upper case alphabets

for index in range(len(input_string)):
    char = input_string[index]
    if char in list_alphabets:  #we need to encrypt only characters, that's why
        encrypted_char = chr(ord(char)+1)   #encrypting to the next alphabet
        input_string[index] = encrypted_char

encrypted_string = "".join(input_string)

print(encrypted_string)