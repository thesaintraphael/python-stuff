def interpolitan_search(arr, target):

    low, high = 0, len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        index = low + \
            int(((float(high - low) /
                (arr[high] - arr[low])) * (target - arr[low])))

        if arr[index] == target:
            return index

        if arr[index] < target:
            low = index + 1

        else:
            high = index - 1

    return -1
