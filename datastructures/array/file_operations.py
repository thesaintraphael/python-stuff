from array import array

arr = array("i", (1, 2, 3))


with open("datastructures/array/tofile.txt", "wb") as file:
    arr.tofile(file)


with open("datastructures/array/tofile.txt", "r") as file:
    print(file.read())


# Note:
# array.tofile(file) writes all items (as machine values)
# to the provided file object
