nums = [-55,0,10,12,16,20,33]
x = int(input('Enter a number:'))

found = False
found_index = -1
lo = 0
hi = len(nums)
while hi > lo:
    mid = (lo + hi) // 2
    num = nums[mid]
    if x == num:
        found = True
    elif x < num:
        hi = mid
    elif x > num:
        lo = mid + 1

if not found:
    print('Not found')
if found:
    print('Found')
