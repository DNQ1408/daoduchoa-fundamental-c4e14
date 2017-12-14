# def add(): # no arguments
#      x = 1
#      y = 2
#      print(x + y)

# def add(x, y):
#     print(x + y)

def evaluate(x, y, op):
    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    elif op == '/':
        result = x / y
    return result

from random import randint,choice

x = randint(0,10)
y = randint(1,10)
op = choice(['+','-','*','/'])

z = evaluate(x, y, op)

# print(z)





# add(3, 4)
# a = 12
# b = 1
# add(a, b)
