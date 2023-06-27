def bubble_sort(number_digits, numbers_list):
    for i in range(number_digits - 1):
        for j in range(0, number_digits - i - 1):
            var1 = numbers_list[j] + numbers_list[j + 1]
            var2 = numbers_list[j + 1] + numbers_list[j]
            if var1 < var2:
                numbers_list[j], numbers_list[j + 1] = (
                    numbers_list[j + 1],
                    numbers_list[j],
                )

    return numbers_list


number_digits = int(input())
numbers_list = input().split(' ')
print(''.join(bubble_sort(number_digits, numbers_list)))
