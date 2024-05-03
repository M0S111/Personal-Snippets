def move_zeros(list):

    #if list.count(0) > 0:
    #for n in list:

    #    list.append(list.pop(list.index(0)))

    [list.append(list.pop(list.index(0))) for n in list if list.count(0) > 0]

    return list

print(move_zeros([1, 7, 0, 2, 0, 1, 3]))
