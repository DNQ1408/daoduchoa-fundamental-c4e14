from turtle import *
speed(-1)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
draw_nb = len(colors)
for i in range (draw_nb):
    color(colors[i])
    a = i + 2
    for j in range (a):
        forward(100)
        left(360 / a)

mainloop()
