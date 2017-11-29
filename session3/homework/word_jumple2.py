from random import shuffle, choice
word_list = ['champion','naruto','computer','exercise']
loop = True
while loop:
    word = choice(word_list)
    characters = list(word)
    shuffle(characters)
    for index, item in enumerate(characters):
        print(item, end=' ')
    answer = str(input('Your answer:'))
    if answer == word:
        print('Nice')
    else:
        print('Try again ')
