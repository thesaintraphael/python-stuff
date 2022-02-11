def bubble_sort(arr):

    for i in range(len(arr)):

        for j in range(0, len(arr) - i - 1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


data = [-2, 45, 0, 11, -9]
bubble_sort(data)
print(data)
