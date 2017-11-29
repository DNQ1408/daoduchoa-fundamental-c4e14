favs = ["reading", "searching", "naruto"]
length = len(favs)
for i in range (length):
    print(i+1, favs[i], sep=', ')
poscontent = str(input("Fav stuff you want to get rid of"))

favs.remove(poscontent)
for i in range (length - 1):
    print(i+1, favs[i], sep=', ')
