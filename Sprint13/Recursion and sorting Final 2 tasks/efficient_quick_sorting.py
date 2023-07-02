# ID 88663653
def quicksort(array, key=None):
    def partition(start, end):
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

    def _quicksort(start, end):
        if start >= end:
            return
        pivot_ind = partition(start, end)
        _quicksort(start, pivot_ind - 1)
        _quicksort(pivot_ind + 1, end)

    _quicksort(0, len(array) - 1)


if __name__ == '__main__':
    players_count = int(input())
    players = []
    for _ in range(players_count):
        login, task, penalty = input().split()
        players.append((login, int(task), int(penalty)))

    quicksort(players, key=lambda player: (-player[1], player[2], player[0]))

    for player in players:
        print(player[0])
