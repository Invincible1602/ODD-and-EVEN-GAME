import random

d = int(input("best of number of matches (1, 3, 5) only: "))
player = 0
computer = 0

for i in range(1, d + 1):
    a = int(input("Enter the number: "))
    b = int(input("Enter the number between 0 and {}: ".format(a)))
    j = input("Enter the choice(Even, Odd): ").capitalize()
    c = random.randint(0, a)

    if j == "Odd":
        if (c + b) % 2 == 0:
            print(c+b)
            print("Computer wins, sorry player one")           
            computer += 1
        else:
            print(c+b)
            print("Computer loses, player wins")
            player += 1

    if j == "Even":
        if (c + b) % 2 == 0:
            print(c+b)
            print("Computer loses, player one wins")                             
            player += 1
        else:
            print(c+b)
            print("Computer wins, sorry player one")
            computer += 1

if computer > player:
    print("Computer is the winner, you lose. Game over.")
else:
    print("Winner Winner Chicken Dinner")
