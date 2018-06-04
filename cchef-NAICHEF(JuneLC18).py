# Author: https://www.github.com/rohegde7 (Rohit Hegde - hegde.rohit7@gmail.com)

#https://www.codechef.com/JUNE18B/problems/NAICHEF
# Problem Code: NAICHEF

# status: All test cases passed :)

no_tests = int(input())

for i in range(no_tests):
    no_dice_sides, diceA, diceB = map(int, input().split())

    list_dice_sides = list(map(int, input().split()))

    #print(no_dice_sides, diceA, diceB, list_dice_sides)

    prob_A = list_dice_sides.count(diceA)/no_dice_sides
    prob_B = list_dice_sides.count(diceB)/no_dice_sides

    prob_winning = prob_A*prob_B    

    print("%.10f" %prob_winning)

