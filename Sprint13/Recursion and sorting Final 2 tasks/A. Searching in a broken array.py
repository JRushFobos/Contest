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


# Updated version
# ID 88662051
def broken_search(array, desired_element):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_element = array[mid]

        if mid_element == desired_element:
            return mid

        if array[left] == desired_element:
            return array[left]

        if array[left] < mid_element:
            if array[left] < desired_element and desired_element < mid_element:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if mid_element < desired_element and desired_element < array[left]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# Final version
# ID 88731975
def broken_search(array, desired_element):
    left, right = 0, len(array) - 1

    while left < right:
        mid = (left + right) // 2
        mid_element = array[mid]

        if mid_element == desired_element:
            return mid

        if array[left] == desired_element:
            return left

        if array[left] < mid_element:
            if array[left] < desired_element and desired_element < mid_element:
                right = mid - 1
            else:
                left = mid + 1
        elif array[left] > mid_element:
            if mid_element < desired_element and desired_element < array[left]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            left += 1

    if left == right and array[left] == desired_element:
        return left

    return -1


# n = 11
# k = 1
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]


# # n = 2
# # k = 1
# # array = [5, 1]

# # n = 5
# # k = 4
# # array = [8, 10, 0, 2, 4]

# result = broken_search(array, k)
# print(result)
