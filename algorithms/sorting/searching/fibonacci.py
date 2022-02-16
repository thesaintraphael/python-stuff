def fibonnacci_search(arr, val):

    fib_minus_2, fib_minus_1 = 0, 1
    fib = fib_minus_1 + fib_minus_2

    while(fib < len(arr)):
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib
        fib = fib_minus_1 + fib_minus_2

    index = -1

    while (fib > 1):
        i = min(index + fib_minus_2, (len(arr)-1))
        if (arr[i] < val):
            fib = fib_minus_1
            fib_minus_1 = fib_minus_2
            fib_minus_2 = fib - fib_minus_1
            index = i
        elif (arr[i] > val):
            fib = fib_minus_2
            fib_minus_1 = fib_minus_1 - fib_minus_2
            fib_minus_2 = fib - fib_minus_1

        else:
            return i

    if(fib_minus_1 and index < (len(arr)-1) and arr[index+1] == val):
        return index + 1
    return -1


print(fibonnacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 6))
