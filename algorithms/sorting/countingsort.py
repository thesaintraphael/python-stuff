def counting_sort(input_arr):
    max_ = max(input_arr)

    count_length = max_ + 1

    # Initialize the countArray with (max+1) zeros
    count_ = [0] * count_length

    # Step 1 -> Traverse the input_arr and increase
    # the corresponding count for every element by 1
    for el in input_arr:
        count_[el] += 1

    # Step 2 -> For each element in the count_,
    # sum up its value with the value of the previous
    # element, and then store that value
    # as the value of the current element
    for i in range(1, count_length):
        count_[i] += count_[i-1]

    # Step 3 -> Calculate element position
    # based on the count_ values
    output_array = [0] * len(input_arr)
    i = len(input_arr) - 1
    while i >= 0:
        current_el = input_arr[i]
        count_[current_el] -= 1
        new_position = count_[current_el]
        output_array[new_position] = current_el
        i -= 1

    return output_array


input_arr = [2, 21, 0, 6, 1, 9, 9, 7]
print("Input array = ", input_arr)

sorted_arr = counting_sort(input_arr)
print("Counting sort result = ", sorted_arr)


"""Counting Sort a stable, non-comparative algorithm.

Non-comparative sorting algorithms perform sorting without any comparison between elements to be sorted."""
