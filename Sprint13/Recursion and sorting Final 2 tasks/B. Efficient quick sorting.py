# ID 88616570
def partition(array, start, end, key):
    count = start - 1
    pivot = array[end]
    step = start
    while step < end:
        if key(array[step]) < key(pivot):
            count += 1
            array[count], array[step] = array[step], array[count]
        step += 1
    array[count + 1], array[end] = array[end], array[count + 1]
    return count + 1


def quicksort(array, start=0, end=None, key=None):
    if end is None:
        end = len(array) - 1
    if start >= end:
        return
    pivot_ind = partition(array, start, end, key)
    quicksort(array, start, pivot_ind - 1, key)
    quicksort(array, pivot_ind + 1, end, key)


players_count = int(input())
players = []
for _ in range(players_count):
    login, task, penalty = input().split()
    players.append((login, int(task), int(penalty)))

quicksort(players, key=lambda x: (-x[1], x[2], x[0]))

for player in players:
    print(player[0])
