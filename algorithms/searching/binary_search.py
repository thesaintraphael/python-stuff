def test_location(numbers, target, mid):
    mid_number = numbers[mid]

    if mid_number == target:
        return "left" if mid > 1 and numbers[mid - 1] == target else "found"
    elif mid_number < target:
        return "left"

    else:
        return "right"


def binary_search(numbers, target):

    first, last = 0, len(numbers) - 1

    while first <= last:
        mid = (first + last) // 2
        result = test_location(numbers, target, mid)

        if result == "found":
            return mid

        elif result == "left":
            last = mid - 1

        else:
            first = mid + 1

    return -1


numbers = [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
print(binary_search(numbers, 6))
