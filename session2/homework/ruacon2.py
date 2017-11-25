from turtle import *

for i in range (4):
    if i%2 == 0:
        color("Blue")
    else:
        color("Red")
    n = i+3
    for x in range(n):
        forward(100)
        left(360/n)

mainloop()
