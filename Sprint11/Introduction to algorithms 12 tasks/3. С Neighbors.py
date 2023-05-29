size_y1 = int(input())
size_x1 = int(input())
matrix = []
for i in range(size_y1):
    row = list(map(int, input().split()))
    matrix.append(row)

coordinate_y2 = int(input())
coordinate_x2 = int(input())

coordinate_y2 = 1
coordinate_x2 = 0

out = []

if 0 <= coordinate_y2 - 1 < len(matrix) and 0 <= coordinate_x2 < len(
    matrix[coordinate_y2]
):
    out.append(matrix[(coordinate_y2 - 1)][coordinate_x2])
if 0 <= coordinate_y2 + 1 < len(matrix) and 0 <= coordinate_x2 < len(
    matrix[coordinate_y2]
):
    out.append(matrix[(coordinate_y2 + 1)][coordinate_x2])
if 0 <= coordinate_y2 < len(matrix) and 0 <= coordinate_x2 + 1 < len(
    matrix[coordinate_y2]
):
    out.append(matrix[coordinate_y2][coordinate_x2 + 1])
if 0 <= coordinate_y2 < len(matrix) and 0 <= coordinate_x2 - 1 < len(
    matrix[coordinate_y2]
):
    out.append(matrix[coordinate_y2][(coordinate_x2 - 1)])

out.sort()
print(' '.join(map(str, out)))
