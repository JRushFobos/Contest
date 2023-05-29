num = int(input())
list_zeros_ones = []

if num == 0:
    list_zeros_ones.append(0)

while num > 0:
    remains = num % 2
    list_zeros_ones.append(remains)
    num = num // 2

print(''.join(map(str, list_zeros_ones[::-1])))
