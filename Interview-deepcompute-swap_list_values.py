list_numbers = list(map(int, input("Enter the numbers for the list\n").split()))

list_size = len(list_numbers)
#swaping:
list_numbers[0], list_numbers[list_size-1] = list_numbers[list_size-1], list_numbers[0]

print("The new list after swapping is:\n", list_numbers)