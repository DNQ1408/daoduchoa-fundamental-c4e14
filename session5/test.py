teencode_dict = {
        'gato': 'Ghen ăn tức ở',
        'wtf': 'What the fuck',
        'r': 'rồi',
        'ik': 'Đi',
        'hk': 'học',
        'cj': 'chị'
    }
while True:
    print("Here's our dictionary")
    for key in teencode_dict:
        print(key, end=' ')
    print()

    code = str(input('What do you want to know?')).lower()
    if code in teencode_dict:
        meanning = teencode_dict[code]
        print(code,':', meanning)

    else:
        print('This word has not been in dict yet')
        command = str(input('Do you want to add it (Y/N)')).lower()

        if command == 'y':
            new_word = code
            new_meanning = str(input('Translation:'))
            teencode_dict[new_word] = 'new_meanning'
        elif command == 'n':
            pass
        else:
            print('Wrong command')

for key in teencode_dict:
    print(key,end=' ')
