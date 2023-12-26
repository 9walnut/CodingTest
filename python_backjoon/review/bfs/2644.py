from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
visit = [0]*(n+1)
graph = [[] for _ in range(n+1)]
result = -1

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(start):
    q = deque()
    q.append((start, 0))
    visit[start] = 1

    while q:
        node, depth = q.popleft()

        if depth == b:
            return depth

        for i in graph[node]:
            if visit[i] == 0:
                visit[i] = 1
                q.append(i, depth+1)


result = bfs(a)

if result is not None:
    print(result)
else:
    print(-1)
