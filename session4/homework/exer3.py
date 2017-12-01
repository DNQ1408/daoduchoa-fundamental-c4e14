n_int = False

while not n_int:
    try:
        n = int(input('Enter a number'))
        n_int = True
    except ValueError:
        print('Not a number')
        
if n < 2:
    print(n, "is not a prime number")
if n == 2:
    print(n, "is a prime number")
for i in range(2,n):
    if n%i == 0:
        print(n, "is not a prime number")
        break
    elif n == i+1:
        print(n, "is a prime number")
