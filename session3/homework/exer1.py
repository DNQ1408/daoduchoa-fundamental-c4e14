shopitems = ['T_Shirt', 'Sweater']


loop_1 = True
while loop_1:
    command = str(input('Welcome to our shop, what do you want (C, R, U, D)?'))
    if command is 'R':
        print('Our items:')
        for index, item in enumerate(shopitems):
            print(item, sep=',')
    elif command is 'C':
        new_item = str(input('Enter new item:'))
        shopitems.append(new_item)
        print('Our items:')
        for index, item in enumerate(shopitems):
            print(item, sep=',')


    elif command is 'U':
        loop_1_1 = True
        while loop_1_1:
            upd_posi = int(input('Update position:'))
            if upd_posi < 1 or upd_posi > len(shopitems):
                print('Out of range')
            else:
                rep_item = str(input('New item:'))
                shopitems[upd_posi - 1] = rep_item
                print('Our items:')
                for index, item in enumerate(shopitems):
                    print(item, sep=',')
                loop_1_1 = False


    elif command is 'D':
        loop_1_2 = True
        while loop_1_2:
            del_posi = int(input('Delete position:'))
            if del_posi < 1 or del_posi > len(shopitems):
                print('Out of range')
            else:
                shopitems.pop(del_posi - 1)
                print('Our items:')
                for index, item in enumerate(shopitems):
                    print(item, sep=',')
                loop_1_2 = False
    elif command is 'E':
        loop_1 = False
    else:
        print('Wrong Command')
