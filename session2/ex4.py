n = int(input("Enter a number:"))
for i in range(2,n):
    if n%i == 0:
        print("Day ko la so nguyen to")
        break
    elif n == i+1:
        print("Day la so nguyen to")
