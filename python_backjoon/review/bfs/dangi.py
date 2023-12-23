def bfs(si, sj):
    q = []
    q.append((si, sj))
    visit[si, sj] = 1
    cnt = 1

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < t and 0 <= nj < t and visit[ni][nj] == 0 and graph[ni][nj] == 1:
                q.append((ni, nj))
                visit[ni][nj] = 1
                cnt += 1


t = int(input())
graph = [list[map(int, input())] for _ in range(t)]
visit = [[0]*t for _ in range(t)]
ans = []

for i in range(t):
    for j in range(t):
        if graph[i][j] == 1 and visit[i][j] == 0:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans), *ans, sep='\n')
