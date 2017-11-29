menu  = ["1", "2", "3"]

print("Hi, here's your menu so far",*menu, sep= ", ") #seperator
menu.append(str(input("Name one thing you want to add?")))
print(*menu, sep= ", ")
