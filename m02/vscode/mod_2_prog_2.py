firstList = [3, 2, 1, 0]

guess_me = int(7)
number = int(1)
weLoop = bool(True)
i = 0

for i in range(len(firstList)):
    print(firstList[i])

while weLoop == True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        weLoop = False
    elif number > guess_me:
        print("oops")
        weLoop = False
    number = number + 1

number = 1
guess_me = 5
for number in range(10):
    if number < guess_me:
        print("too low (for)")
    elif number == guess_me:
        print("found it! (for)")
        break
    elif number > guess_me:
        print("oops (for)")
        break