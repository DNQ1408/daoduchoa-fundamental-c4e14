from random import *
rdnb = randint(1,100)
guess = 0
manxnbofguess = int(input("Number of guess:"))
guess_wrong = True

while True:
    usernb = int(input("Guess my number(1,100):"))
    if usernb < rdnb:
        print("Too small" )
    elif usernb > rdnb:
        print("Too large" )
    else:
        print("Bingo")
        break
    guess += 1
    if guess == maxnbofguess :
        print("Game Over")
        break
