stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack)  # [1, 2, 3]


print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1
# print(stack.pop())  # IndexError: pop from an empty list
