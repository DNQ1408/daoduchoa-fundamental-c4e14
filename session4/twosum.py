nums = [-11,10,0,3,4,5,12,7,-10,9]

found = False
for i in range (0,len(nums))
    x1 = nums[0]
    x2 = 0
    for j in range (i + 1,len(nums)):
        if x1 + num[j] == 0:
            x2 = nums[j]
            found = True
            break
if found:
    print('Found {0} and {1}'.format(x1, x2))
