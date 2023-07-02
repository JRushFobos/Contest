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
