from collections import deque

# double-enden queue

deque()  # deque([])
deque(['a', 'b', 'c'])
deque("abc")  # deque(['a', 'b', 'c']) same as previous
deque([{'data': "a"}, {"data": "b"}])


deq = deque(['a', 'b', 'c'])
deq.append(5)  # appends to the end
deq.appendleft(0)  # appends to the start of the deq

print(deq)

last_element = deq.pop()  # removes last element and returns it

first_element = deq.popleft()  # removes first element and returns it


print(deq)


# It is possible to implement queues and stack with deque
