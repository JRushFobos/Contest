# Мониторинг
def transpose_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])

    transposed_matrix = []
    for j in range(n):
        row = []
        for i in range(m):
            row.append(matrix[i][j])
        transposed_matrix.append(row)

    return transposed_matrix


n = int(input())
m = int(input())

if n != 0 or m != 0:
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    transposed = transpose_matrix(matrix)

    for row in transposed:
        print(' '.join(map(str, row)))
