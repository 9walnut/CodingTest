# 2164 -  카드2
from collections import deque

n = int(input())
dq = deque([i for i in range(1, n+1)])

while (len(dq) > 1):
    dq.popleft()
    result = dq.popleft()
    dq.append(result)

print(dq[0])
