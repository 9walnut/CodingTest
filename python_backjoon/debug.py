from collections import deque

t = int(input())
a, b = map(int, input().split())
link = int(input())
visited = [0]*(t+1)
graph = [[] for i in range(t+1)]
result = -1

for i in range(link):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(start):
    q = deque()
    q.append((start, 0))
    visited[start] = 1

    while q:
        node, depth = q.popleft()

        if node == b:
            return depth

        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                q.append((i, depth+1))


result = bfs(a)

if result is not None:
    print(result)
else:
    print(-1)
