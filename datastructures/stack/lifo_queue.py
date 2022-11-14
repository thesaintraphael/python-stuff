# lthread-safe stack implementation using a LifoQueue


from queue import LifoQueue

stack = LifoQueue()

stack.put(1)
stack.put(2)
stack.put(3)


print(stack.get())  # 3
print(stack.get())  # 2
print(stack.get())  # 1
# print(stack.get())  # Waits forever
print(stack.empty())  # True
# print(stack.get_nowait())  # Raises queue.Empty if stack is empty


"""

NOTES:
    Lists are not thread safe.
    Deques are thread safe, but only you limited yourself to operations append() and pop().
    LifoQueue is thread safe and you can use all operations.
    So, if you need a thread safe stack, use LifoQueue.

"""
