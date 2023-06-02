# ID 87889835
from typing import List


def score_counter(k: int, keyboard_buttons: List[str]) -> int:
    points = 0
    numbers = {}
    for row in keyboard_buttons:
        for number in row:
            if number.isdigit():
                numbers.setdefault(number, 0)
                numbers[number] += 1
    for point in numbers.values():
        if point <= k:
            points += 1
    return points


if __name__ == '__main__':
    k = int(input()) * 2
    keyboard_buttons = [input() for button in range(4)]
    print(score_counter(k, keyboard_buttons))
