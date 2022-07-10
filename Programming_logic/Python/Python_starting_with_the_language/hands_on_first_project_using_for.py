import random

print("*****************************")
print("welcome to the guesswork game")
print("*****************************")

randomNumber = (random.randint(0, 100))
max_trys = 0
round = 1

print("what's the difficulty?")
print("(1) easy, (2) medium, (3) hard, (4) nightmare.")

level = int(input("define the difficulty: "))

if(level == 1):
    max_trys = 20
    print("You chosed the easy level, you have 20 try's, good luck!")

elif(level == 2):
    max_trys = 10
    print("You chosed the medium level, you have 10 try's, it's in your own risk")

elif(level == 3):
    max_trys = 5
    print("You chosed the hard level, you have 5 try's, i'll say nothing")
else:
    (level == 4)
    max_trys = 1
    print("You chosed the nightmare level, you have 1 try, :D")

print(randomNumber)

while(level <= 4):
    print("try {} of {}".format(round, max_trys))
    guess_str = input("type a number between 1 and 100 ")
    print("You type, " + guess_str)
    guess = int(guess_str)

if(guess <= 4 ):
     

print("END of the game!")
