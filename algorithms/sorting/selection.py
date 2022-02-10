numbers = [64, 25, 12, 22, 11]


def sort_arr(arr):

    for i in range(len(arr)):

        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


sort_arr(numbers)
print(numbers)

# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

# 1) The subarray which is already sorted.
# 2) Remaining subarray which is unsorted.

# In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.
