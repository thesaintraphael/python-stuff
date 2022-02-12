def quick_sort(A):
    quick_sort_main(A, 0, len(A) - 1)


def quick_sort_main(A, low, high):

    if low < high:
        pivot = partition(A, low, high)
        quick_sort_main(A, low, pivot-1)
        quick_sort_main(A, pivot+1, high)


def get_pivot(A, low, high):

    # in this case pivot is Median of tree

    mid = (high + low) // 2
    pivot = high

    if A[low] < A[mid]:
        if A[mid] < A[high]:
            pivot = mid
    elif A[low] < A[high]:
        pivot = low

    return pivot


def partition(A, low, high):

    pivot_index = get_pivot(A, low, high)
    pivot_value = A[pivot_index]

    A[pivot_index], A[low] = A[low], A[pivot_index]
    border = low

    for i in range(low, high+1):
        if A[i] < pivot_value:
            border += 1
            A[i], A[border] = A[border], A[i]

    A[low], A[border] = A[border], A[low]

    return border


A = [5, 9, 1, 2, 4, 8, 6, 3, 7]
print(A)
quick_sort(A)
print(A)
