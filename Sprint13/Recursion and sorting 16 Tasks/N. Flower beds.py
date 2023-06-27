# Клумбы
def merge_segments(segments):
    # Сортируем отрезки по начальной точке
    segments.sort(key=lambda x: x[0])

    merged_segments = []
    current_segment = segments[0]

    for i in range(1, len(segments)):
        if segments[i][0] <= current_segment[1]:
            # Если текущий отрезок перекрывается с следующим, объединяем их
            current_segment[1] = max(current_segment[1], segments[i][1])
        else:
            # Если текущий отрезок не перекрывается с следующим, добавляем его в результат и обновляем текущий отрезок
            merged_segments.append(current_segment)
            current_segment = segments[i]

    # Добавляем последний объединенный отрезок или последний отрезок, если не было объединения
    merged_segments.append(current_segment)

    return merged_segments


# Пример ввода
# segments = [[7, 8], [7, 8], [2, 3], [6, 10]]
# 2 3
# 6 10

# segments = [[2, 3], [5, 6], [3, 4], [3, 4]]
# 2 4
# 5 6
# Объединяем отрезки
segments = []

n = int(input())
for _ in range(n):
    start, end = map(int, input().split())
    segments.append([start, end])

merged = merge_segments(segments)

# Вывод результата
for segment in merged:
    print(segment[0], segment[1])
