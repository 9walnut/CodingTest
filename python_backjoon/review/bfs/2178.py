# 미로탐색

def bfs(si, sj, ei, ej):
    q = []
    visit = [[0]*m for _ in range(n)]
    q.append((si, sj))
    visit[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        if (ci, cj) == (ei, ej):
            return visit[ci][cj]
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < n and 0 <= nj < m and visit[ni][nj] == 0 and graph[ni][nj] == 1:
                q.append((ni, nj))
                visit[ni][nj] = visit[ci][cj] + 1


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
answer = bfs(0, 0, n-1, m-1)
print(answer)
