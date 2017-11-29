from random import shuffle
word = 'champion'
characters = list(word)
shuffle(characters)
for index, item in enumerate(characters):
    print(item, end=' ')
answer = str(input('Your answer:'))
if answer == word:
    print('Nice')
else:
    print('Try again ')
