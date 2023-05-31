# ID 87832924
k = int(input()) * 2
keyboard = [input() for button in range(4)]

numbers_dict = {}
points = 0

for row in keyboard:
    for number in row:
        if number.isdigit():
            if number in numbers_dict:
                numbers_dict[number] += 1
            else:
                numbers_dict[number] = 1
print(numbers_dict)
for point in numbers_dict.values():
    if point <= k:
        points += 1

print(points)
