# ID 87889701
from typing import List


def distance_to_zero(addresses_houses: List[int], max_index) -> List[int]:
    zeros = [
        index for index, value in enumerate(addresses_houses) if value == 0
    ]
    distances = [0] * max_index
    first_zero = zeros[0]
    distances[:first_zero] = [
        first_zero - distance for distance in range(first_zero)
    ]
    for left_zero_index, right_zero_index in zip(zeros, zeros[1:]):
        for index in range(left_zero_index + 1, right_zero_index):
            distances[index] = min(
                index - left_zero_index, right_zero_index - index
            )
    last_zero = zeros[-1]
    distances[last_zero + 1 :] = [
        pos - last_zero for pos in range(last_zero + 1, len(addresses_houses))
    ]
    return distances


if __name__ == '__main__':
    max_index = int(input())
    addresses_houses = [int(address) for address in input().split()]
    print(*distance_to_zero(addresses_houses, max_index))
