def linear_search(numbers, target):

    return next(
        (index for index, number in enumerate(numbers) if number == target), -1
    )


numbers = [1, 49, 56, 3, 355]
print(linear_search(numbers, 355))
print(linear_search(numbers, 50))
