nums = [1,3,5,18,12, -45]

min_num = 1
for num in nums:
    if min_num >= num:
        min_num = num
print('Min number', min_num)
