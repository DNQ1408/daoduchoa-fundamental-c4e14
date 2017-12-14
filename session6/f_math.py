# import calc
# result = calc.evaluate(1,3,'*')
# print(result)

# from calc import evaluate
#
# result = evaluate(1, 3,'+')
# print(result)

from calc import *
from random import *

x = randint(0,10)
y = randint(1,10)
op = choice(['+']*50 + ['-'] * 25 + ['*'] *10 + ['/'] *15)
error = randint(-1,1)

result = evaluate(x,y,op) + error
print('{0} {1} {2} = {3}'.format(x,op,y,result))
answer = str(input('Y/N')).lower()

if 'y' in answer:
    if error = 0:
        print('Yay')
    else:
        print('Haiz')
if 'n' in answer:
    if error != 0:
        print('Yay')
    else:
        print('Haiz')
