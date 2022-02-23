def binary_search(numbers, target):

    first, last = 0, len(numbers) - 1
    index = -1

    while first <= last and index == -1:
        mid = (first + last) // 2
        if numbers[mid] == target:
            index = mid
        elif target < numbers[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return index


numbers = [1, 2, 3, 4, 5]
print(binary_search(numbers, 4))
print(binary_search(numbers, 6))
