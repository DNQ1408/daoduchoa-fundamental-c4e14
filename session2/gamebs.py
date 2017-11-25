from random import randint


luc = int(input("Your luck level?"))
agi = int(input("Your agility level?"))
x = randint(1,6)
if x< luc + agi:
    print("You have been hit")
else:
    print("Missed Attack")
