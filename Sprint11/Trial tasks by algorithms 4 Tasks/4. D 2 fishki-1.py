# Тестовые данные
# 6 всего фишек                    -1 3
# -1 -1 -9 -7 3 -6 наминал фишек
# 2 сумма для пары


def two_sum(arr, target_sum):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                return arr[i], arr[j]
    return [None]


n = int(input())
arr = list(map(int, input().split()))
target_sum = int(input())

print(' '.join(map(str, two_sum(arr, target_sum))))
