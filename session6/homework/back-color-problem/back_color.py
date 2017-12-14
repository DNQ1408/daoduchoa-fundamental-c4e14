from random import *
from ex11_12 import is_inside

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    text_list= ['BLUE', 'RED', 'YELLOW', 'GREEN']
    color_list = ['#3F51B5', '#C62828', '#FFD600', '#4CAF50']
    text = choice(text_list)
    color = choice(color_list)
    return [
                text,
                color,
                randint(0, 1) # 0 : meaning, 1: color
            ]



def mouse_press(x, y, text, color, quiz_type):
    click = [x, y]

    for dic in shapes:
        rec = dic['rect']
        if is_inside(click, rec):
            color_click = dic['color']
            text_click = dic['text'].upper()
    if quiz_type == 0:
        return text_click == text

    if quiz_type == 1:
        return color_click == color
