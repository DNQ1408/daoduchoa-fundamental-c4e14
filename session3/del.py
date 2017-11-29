favs = ["reading", "searching", "naruto"]
length = len(favs)
for i in range (length):
    print(i+1, favs[i], sep=', ')

posdel = int(input("Position you want to get rid of:")) - 1
loop = True

while loop:
    if posdel < 1 or posdel > length:
        print(" Out of range")
        posdel = int(input("Position you want to get rid of:")) - 1
    else:
        favs.pop(posdel)
        for i in range (length - 1):
            print(i+1, favs[i], sep=', ')
        loop = False
