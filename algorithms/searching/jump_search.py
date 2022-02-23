import math


def jump_search(arr, target):

    length = len(arr)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and arr[left] <= target:
        right = min(length - 1, left + jump)
        if arr[right] >= target:
            break
        left += jump
    if left >= length or arr[left] > target:
        return -1
    right = min(length - 1, right)

    while left <= right and arr[left] <= target:
        if arr[left] == target:
            return left

        left += 1

    return -1


arr = [0, 1, 2, 3, 4]
target = 3

print(jump_search(arr, target))
