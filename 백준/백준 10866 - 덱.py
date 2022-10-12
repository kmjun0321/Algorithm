import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
for _ in range(n):
  command = sys.stdin.readline().strip()
  if "push_back" in command:
    arr = command.split()
    queue.append(arr[1])
  elif "push_front" in command:
    arr = command.split()
    queue.appendleft(arr[1])
  elif command == "pop_front":
    if len(queue) > 0:
      print(queue.popleft())
    else:
      print(-1)
  elif command == "pop_back":
    if len(queue) > 0:
      print(queue.pop())
    else:
      print(-1)
  elif command == "size":
    print(len(queue))
  elif command == "empty":
    if len(queue) > 0:
      print(0)
    else:
      print(1)
  elif command == "back":
    if len(queue) > 0:
      print(queue[len(queue)-1])
    else:
      print(-1)
  elif command == "front":
    if len(queue) > 0:
      print(queue[0])
    else:
      print(-1)
