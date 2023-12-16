# 연결 요소의 개수
from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph, start, visit):
    q = deque()
    visit[start] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visit[i]:
                q.append(i)
                visit[i] = True


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visit = [False]*(n+1)

for i in range(1, n+1):
    if not visit[i]:
        bfs(graph, i, visit)
        count += 1
print(count)
