# 토마토
from collections import deque


def bfs():
    q = deque()
    visited = [[0]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i, j))
                visited[i][j] = 1
            elif graph[i][j] == 0:
                cnt += 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and graph[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
                cnt -= 1

    if cnt == 0:
        return visited[ci][cj] - 1
    else:
        return -1


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = bfs()
print(answer)
