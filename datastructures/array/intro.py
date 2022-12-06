from array import array


arr = array("I", [1, 2, 3])
# "I" means unsingned int, any other data type will raise an error

# arr = array("I", [1, -1]) OverflowWrror: can't convert negative value to unsigned int

print(arr)  # array('I', [1, 2, 3])

for number in arr:
    print(f"{number=}")

print(arr[0])  # 1

arr.append(4)
print(arr.count(4))  # 1
print(arr.index(1))  # 0
