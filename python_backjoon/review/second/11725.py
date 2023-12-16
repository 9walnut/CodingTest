# 트리의 부모찾기
import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)

ans = [0]*n+1


def bfs():
    while q:
        now = q.popleft
        for nxt in graph[now]:
            if ans[nxt] == 0:
                ans[nxt] = now
                q.append(nxt)


bfs()
res = ans[2:]
for x in res:
    print(x)
