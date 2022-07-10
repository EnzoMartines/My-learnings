import random

print("*****************************")
print("welcome to the guesswork game")
print("*****************************")

randomNumber = (random.randint(0, 100))
max_trys = 3
round = 1

print(randomNumber)

while(round <= max_trys):
    print("try {} of {}".format(round, max_trys))
    guess_str = input("Type your number between 1 and 100: ")
    print("You typed " + guess_str)
    guess = int(guess_str)

    if(guess < 1 or guess > 100):
        print("You need to type a number between 1 and 100!!!")
        continue

    areRight = guess == randomNumber
    higher = guess < randomNumber
    lower = guess > randomNumber

    if(areRight):
        print("You're right")
        break
    else:
        if(higher):
            print("You're wrong, the thinked number is higher than you thinked.")
        elif(lower):
            print("You're wrong, the thinked number is lower than you thinked.")
        round = round + 1


print("END of the game!")
