def binary_search(arr, low, high, target):

    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            return binary_search(arr, low, mid-1, target)

        elif arr[mid] < target:
            return binary_search(arr, mid + 1, high, target)

    else:
        return - 1


numbers = [1, 2, 3, 4, 5]
print(binary_search(numbers, 0, len(numbers) - 1, target=4))
print(binary_search(numbers, 0, len(numbers) - 1, target=6))
