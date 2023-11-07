from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]
parent = [0]*(n+1)

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(v):
    que = deque()
    while que:
        x = que.popleft()
        for i in graph[x]:
            if not visited[i]:
                parent[i] = x
                que.append(i)
                visited[i] = True


bfs(1)
for i in range(2, n+1):
    print(parent[i])
