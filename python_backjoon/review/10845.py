# 큐
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for i in range(n):
    arr = list(input().split())
    if arr[0] == "push":
        q.append(arr[1])
    elif arr[0] == "pop":
        if len(q) > 0:
            tmp = q.popleft()
            print(tmp)
        else:
            print(-1)
    elif arr[0] == "empty":
        if len(q) > 0:
            print(0)
        else:
            print(1)
    elif arr[0] == "size":
        print(len(q))
    elif arr[0] == "front":
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif arr[0] == "back":
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)
