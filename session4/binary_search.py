nums = [-55,0,10,12,16,20,33]
x = int(input('Enter a number:'))

found = False
lo = 0
hi = len(nums)
while lo < hi and not found:
    mid = (lo + hi) // 2
    num = nums[mid]
    if x == num:
        found = True
    elif x < num:
        hi = mid # hi = mid - 1 với điều kiện đầu hi = len() - 1 và while lo < hi
    else:
        lo = mid + 1

if not found:
    print('Not found')
if found:
    print('Found')
