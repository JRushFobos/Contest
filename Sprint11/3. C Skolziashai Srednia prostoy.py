# тестовые дынные
# 9
# 9 3 2 0 1 5 1 0 0
# 3
# Вывод программы
# 4.666666666666667 1.6666666666666667 1.0
# Правильный ответ
# 4.6666666667 1.666666667 1 2 2.333333335 2 0.3333333

n = int(input())
list1 = list(map(int, input().split()))
k = int(input())

result = []
for begin_index in range(0, len(list1) - k + 1):
    end_index = begin_index + k
    current_sum = 0
    for v in list1[begin_index:end_index]:
        current_sum += v
    current_avg = current_sum / k
    result.append(current_avg)

result_str = ' '.join(str(x) for x in result)
print(result_str)
