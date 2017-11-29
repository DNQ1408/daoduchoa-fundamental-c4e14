from turtle import *
speed(-1)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
draw_nb = len(colors)
for i in range (draw_nb):
    color(colors[i])
    begin_fill()
    for j in range (2):
        forward(100)
        right(90)
        forward(200)
        right(90)
    end_fill()
    forward(100)
mainloop()
