# Последовательность
def is_subsequence(s, t):
    i = 0
    j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)


# Ввод строк s и t
s = input()
t = input()

# Проверка, является ли s подпоследовательностью t
result = is_subsequence(s, t)

# Вывод результата
print(result)
