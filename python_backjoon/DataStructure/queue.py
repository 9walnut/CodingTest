import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
q = deque()

for _ in range(N):
    command = list(input().split())
    if command[0] == 'push':
        q.append(command[1])
    elif command[0] == 'pop':
        if len(q) > 0:
            tmp = q.popleft()
            print(tmp)
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if len(q) > 0:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)

# 요세푸스 0 - 11866

n, k = map(int, sys.stdin.readline().split())
q = ([i+1 for i in range(n)])
print('<', end='')
for i in range(n):
    for j in range(k-1):
        q.append(q.popleft())
    print(q.popleft(), end='')
    # 마지막이 아닌 숫자에 ', ' 추가해주는 조건문
    if (i != n-1):
        print(',', end=' ')
print('>',)

# 요세푸스 문제 - 1158
n, k = map(int, sys.stdin.readline().split())
q = deque()
result = []
for i in range(1, n+1):
    q.append(i)

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())
print(str(result).replace('[', '<').replace(']'), '>')
