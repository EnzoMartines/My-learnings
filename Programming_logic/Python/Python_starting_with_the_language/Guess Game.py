import random

print("*****************************")
print("welcome to the guesswork game")
print("*****************************")

randomNumber = (random.randint(0, 100))
max_trys = 0
round = 1
nightMareRound = 999

print("what's the difficulty?")
print("(1) easy, (2) medium, (3) hard, (4) nightmare.")

level = int(input("define the difficulty: "))

if(level == 1):
    max_trys = 20
    print("You choosed the easy level, you have 20 try's, good luck!")

elif(level == 2):
    max_trys = 10
    print("You choosed the medium level, you have 10 try's, it's in your own risk")

elif(level == 3):
    max_trys = 5
    print("You choosed the hard level, you have 5 try's, i'll say nothing")
else:
    (level == 4)
    max_trys = 1
    print("$*###&&&@!")

print(randomNumber)

for round in range(1, max_trys + 1):

    if(level == 4):
        print("tRy {} o0f error".format(nightMareRound,))
        guessNightmare_str = input("tYPE ^^&*^#@@")
        guessNightmare = int(guessNightmare_str)
    else:
        print("try {} of {}".format(round, max_trys))
        guess = input("Type your number between 1 and 100: ")
        print("You typed " + guess)
        guess = int(guess)

    if(level == 4):

        (guessNightmare <= 1 or guessNightmare >= 100)
        print("y0u N33D t0 typ3 4 NUmb3R b3tw3en 1 and 1OO$$$")

    else:
        guess < 1 or guess > 100
        print("You need to type a number between 1 and 100!!!")

    if(level == 4):
        nightMareAreRight = guessNightmare == randomNumber
        nightMareIsHigher = guessNightmare < randomNumber
        nightMareIsLower = guessNightmare > randomNumber
    else:
        areRight = guess == randomNumber
        higher = guess < randomNumber
        lower = guess > randomNumber

    if(nightMareIsHigher or nightMareIsLower):
        print("You're dead")

    else:
        (nightMareAreRight)
        print("You're aliv...")
        break

    if(higher):
        print("You're wrong, the thinked number is higher than you thinked.")

    elif(lower):
        print("You're wrong, the thinked number is lower than you thinked.")
        round = round + 1

    else:
        (areRight)
        print("You're right")
        break

print("END of the game!")
