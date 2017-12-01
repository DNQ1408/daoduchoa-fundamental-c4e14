seq_number = [1, 2, 3, 4, 5 ,6 ,7,8,9,10]
user_number =int(input('Enter a number:'))

found = False
found_index = -1
#find_first:
for index, item in enumerate(seq_number):
    if user_number == item:
        found_index = index
        found = True
        break
if not found:
    print('Not found')
else:
    print('Found {0} at index {1}'.format(user_number, found_index))
