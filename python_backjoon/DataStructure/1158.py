# 요세푸스 문제
from collections import deque
import sys

input = sys.stdin.readline


n, k = map(int, input().split())
q = deque()
result = []
for i in range(1, n+1):
    q.append(i)

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())
print(str(result).replace('[', '<').replace(']', '>'))
