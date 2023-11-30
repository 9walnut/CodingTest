# 경로 찾기 - bfs
from collections import deque
n = int(input())
visited = [[0]*n for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]


def bfs(x):
    que = deque()
    que.append(x)
    check = [0 for _ in range(n)]

    while que:
        q = que.popleft()
        for i in range(n):
            if check[i] == 0 and graph[q][i] == 1:
                que.append(i)
                check[i] = 1
                visited[x][1] = 1


for i in range(0, n):
    bfs(i)

for i in visited:
    print(*i)
