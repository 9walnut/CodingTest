# 연결 요소의 개수
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)
cnt = 0

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(start):
    q = deque([start])
    q.append(start)
    visit[start] = 1

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visit[i]:
                q.append(i)
                visit[i] = 1


for i in range(1, n+1):
    if not visit[i]:
        bfs(i)
        cnt += 1

print(cnt)
