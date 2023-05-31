# ID 87819812
from math import inf

max_index = 5
address_list = [6, 7, 0, 6, 1, 2, 0, 1, 2, 0, 5]


def nearzero(address_list):
    r = inf
    right_list = []
    for i in address_list:
        if i != 0:
            right_list.append(r)
            r += 1
        else:
            right_list.append(0)
            r = 1

    l = inf
    left_list = []
    for i in address_list[::-1]:
        if i != 0:
            left_list.append(l)
            l += 1
        else:
            left_list.append(0)
            l = 1

    for x in range(len(left_list)):
        if right_list[x] > left_list[len(left_list) - 1 - x]:
            right_list[x] = left_list[len(left_list) - 1 - x]

    return right_list


address_list = [0, 1, 4, 9, 0]
address_list = [0, 7, 9, 4, 8, 20]
address_list = [0, 1, 4, 8, 0, 8]
print(''.join(map(str, nearzero(address_list))))
