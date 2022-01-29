from collections import deque
import queue


n = int(input())

queue_name = deque([i for i in range(1, n+1)])
print(queue_name)
