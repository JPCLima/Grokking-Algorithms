def lookForKey(box):
    for item in box:
        if item.is_a_box():
            lookForKey(item)
        elif item.is_a_key():
            print("Found the Key!!")


def fact(x):
    if x == 0:
        return 1
    else:
        return x*fact(x-1)


def sum_list(list_n):
    if list_n == []:
        return 0
    else:
        return sum_list(list_n[0:])


print(fact(20))
print(sum_list([1, 2, 3, 4, 5]))
