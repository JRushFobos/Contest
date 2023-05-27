def even_odd(numbers):
    if numbers[0] % 2 == 0 and numbers[1] % 2 == 0 and numbers[2] % 2 == 0:
        return 'WIN'
    elif numbers[0] % 2 != 0 and numbers[1] % 2 != 0 and numbers[2] % 2 != 0:
        return 'WIN'
    else:
        return 'FAIL'


numbers = list(map(int, input().split()))
print(even_odd(numbers))
