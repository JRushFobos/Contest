# ID 88617069
def broken_search(array, desired_element):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == desired_element:
            return mid

        if array[left] <= array[mid]:
            if array[left] <= desired_element < array[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if array[mid] < desired_element <= array[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


# n = int(input())
# k = int(input())
# array = list(map(int, input().split()))

# result = broken_search(array, k)
# print(result)
