def insertion_sort(arr):

    for step in range(1, len(arr)):
        key = arr[step]  # storing element of at the step here
        j = step - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1

        arr[j+1] = key


data = [9, 5, 1, 4, 3]
insertion_sort(data)
print("Sorted", data)


# An insertion sort compares values in turn, starting with the second value in the list.
# If this value is greater than the value to the left of it, no changes are made. Otherwise this
# value is repeatedly moved left until it meets a value that is less than it.
# The sort process then starts again with the next value.
