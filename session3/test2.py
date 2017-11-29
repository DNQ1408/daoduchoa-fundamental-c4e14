favs = ["reading", "searching", "naruto"]
length = len(favs)
# for i in range (length):
# for i, fav in enumerate(favs):
    # print(i+1, fav, sep= ', ')
# for item in favs:
#     print(item)
#
# pos = int(input("Position you want to update")) - 1
# favs[pos] = str(input(" Your repalcing favorite:"))
#
# for i in range (length):
#     print(i+1, favs[i], sep= ', ')
print(*favs)
favs.pop(2)
del favs[0]
#remove
print(*favs)
