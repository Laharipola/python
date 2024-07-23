from collections import deque
numbers=[1,2,3,4]
numbers=deque(numbers)
numbers.popleft()
print(numbers)