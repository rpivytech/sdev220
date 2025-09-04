import random

secret = random.randint(1,10)
guess = int(0)
chooseMode = int(0)
doStuff = bool(True)
small = bool(True)
green = bool(True)
produce = ["Cherry","Pea","Watermelon","Pumpkin"]

while doStuff == True:
    chooseMode = int(input("Please enter a 1 to play number game, enter 2 to do produce thing, or 3 to quit: "))
    while chooseMode == 1 and guess != 100:
        # 4.1
        guess = int(input("Enter your guess (1-10), or enter 100 to return to mode select."))
        if guess > secret:
            print("Guess too high!")
        elif guess < secret:
            print("Guess too low!")
        elif guess == secret:
            print("Correct guess! Enter 100 to return to mode select, or enter 1 to play again.")
            guess = int(input())
            if guess == 1:
                secret = random.randint(1,10)
            elif guess == 100:
                chooseMode = 0
    if chooseMode == 2:
        # 4.2
        # This one is kind of confusing exactly what is being asked of us to do, so I'm just going to try and interpret it.
        i = int(0)
        for i in range (3):
            if produce[i] == "cherry":
                small = bool(True)
                green = bool(False)
            elif produce[i] == "pea":
                small = bool(True)
                green = bool(True)
            elif produce[i] == "watermelon":
                small = bool(False)
                green = bool(True)
            elif produce[i] == "pumpkin":
                small = bool(False)
                green = bool(False)
            print(produce[i], "is it small?", small, "is it green?", green)
    if chooseMode == 3:
        doStuff = False
            
        