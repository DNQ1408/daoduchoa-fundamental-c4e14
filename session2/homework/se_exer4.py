n = int(input("A number, please:"))
for i in range(n):
    print(end="*")

for i in range(n):
    print(end="X*")

c = int(input("Number of columns:"))
r = int(input("Number of rows:"))
for i in range(r):
    for i in range (c):
        print(end="*")
    print()

for i in range (r):
    if i % 2 == 0:
        for x in range(c):
            print(end="X*")
    else:
        for x in range(c):
            print(end="*X")
    print()
