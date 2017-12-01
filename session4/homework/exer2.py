numbers  = [-78, -30, -15, 0, 7, 19, 21, 101, 101, 0, 0]
x_int = False

while not x_int:
    try:
        x = int(input('Enter a number'))
        x_int = True
    except ValueError:
        print('Not a number')

count = numbers.count(x)
print('{0} appear {1} times in my list'.format (x, count))
