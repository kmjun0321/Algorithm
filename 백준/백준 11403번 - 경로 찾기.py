import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
dir = []
for i in range(n):
  dir.append([])
  lst = list(map(int, input().split()))
  for j in range(len(lst)):
    if lst[j] == 1:
      dir[i].append(j)

def check(a, b):
  q = deque()
  q.append(a)
  result = 0
  visited = [0] * n
  while q:
    now = q.popleft()
    visited[now] = 1
    if dir[now]:
      for i in dir[now]:
        if i == b:
          result = 1
          break
        if visited[i] == 0:
          q.append(i)
    if result == 1:
      break
  return result
  
for i in range(n):
  for j in range(n):
    print(check(i, j), end=' ')
  print()

  
'''
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
data = []
for _ in range(n):
  data.append(list(map(int, input().split())))

for k in range(n):
  for i in range(n):
    for j in range(n):
      if data[i][k] == 1 and data[k][j] == 1:
        data[i][j] = 1

for i in range(n):
  for j in range(n):
    print(data[i][j], end=' ')
  print()
'''
