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
