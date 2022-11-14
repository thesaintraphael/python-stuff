from collections import deque


stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print(stack)  # deque([1, 2, 3])


print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1
# print(stack.pop())  # IndexError: pop from an empty deque


# The constant time .append() and .pop() operations
# make deque an excellent choice for implementing a Python stack if your code doesn’t use threading.
