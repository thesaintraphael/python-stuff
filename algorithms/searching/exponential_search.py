from binary_search import binary_search


def exponnential_search(arr, target):

    if arr[0] == target:
        return 0

    index = 1
    while index < len(arr) and arr[index] <= target:
        index *= 2

    return binary_search(arr[:min(index, len(arr))], target)


if __name__ == "__main__":

    print(exponnential_search([1, 2, 3, 4, 5, 6, 7, 8], 3))
