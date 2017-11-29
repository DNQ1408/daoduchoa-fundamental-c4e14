ship_sizes = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name is Duc Hoa and these are my ship size', ship_sizes)

# biggest_size = max(ship_sizes)
# print('Now my biggest ship has size', biggest_size, "Let's shear it")
#
# index_size = ship_sizes.index(biggest_size)
# ship_sizes[index_size] = 8
# print('After shearing, hear is my flock:', ship_sizes)

i = 0
fl_list = []
loop = True
while loop:
    i += 1
    new_flock = [x + 50*(i+1) for x in ship_sizes]
    print ('Month', i, end=':')
    print()
    print ('One month has passed, now is the new flock', new_flock)

    biggest_size = max(new_flock)
    print('Now my biggest ship has size', biggest_size, "Let's shear it")
    index_size = new_flock.index(biggest_size)
    new_flock[index_size] = 8
    print('After shearing, hear is my flock:', new_flock)
    print('*' * 30)
    command = input('Do you want to make 1-month-time-travel (Y/N)')
    if command is 'Y' or command is 'y':
        pass
    elif command is 'N' or command is 'n':
        loop = False

total = sum(new_flock)
print('My flock has size in total:', total)
print('I would get', total, '* 2$ =', total * 2, '$')
