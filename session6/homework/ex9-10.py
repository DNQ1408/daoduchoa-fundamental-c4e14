def get_even_list (li):
    for item in li:
        if item % 2 != 0:
            li.remove(item)
    return li
even_list = get_even_list([1, 2, 5, -10, 9, 6])
print(even_list)
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
