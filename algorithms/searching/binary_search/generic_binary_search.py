# Find first and last positions of numbers in a list

from typing import Callable, Tuple


def first_position(nums: list, target: int) -> int:
    def condition(mid: int):
        if nums[mid] == target:
            return "left" if mid > 0 and nums[mid - 1] == target else "found"
        elif nums[mid] < target:
            return "left"
        else:
            return "right"

    return binary_search(0, len(nums) - 1, condition)


def last_position(nums: list, target: int) -> int:
    def condition(mid: int):
        if nums[mid] == target:
            return (
                "right" if mid < len(nums) - 1 and nums[mid + 1] == target else "found"
            )
        elif nums[mid] < target:
            return "right"
        else:
            return "left"

    return binary_search(0, len(nums) - 1, condition)


def first_and_last_positions(nums: list, target: int) -> Tuple[int, int]:
    return first_position(nums, target), last_position(nums, target)


def binary_search(first: int, end: int, check_condition: Callable) -> int:
    while first <= end:
        mid = (first + end) // 2
        result = check_condition(mid)
        if result == "found":
            return mid
        elif result == "left":
            end = mid - 1
        else:
            first = mid + 1
    return -1


if __name__ == "__main__":
    numbers = numbers = [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
    print(first_and_last_positions(numbers, 6))
