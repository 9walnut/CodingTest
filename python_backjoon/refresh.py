#  토마토
from collections import deque


def bfs():
    q = deque()
    visited = [[[0]*M for _ in range(N)] for _ in range(M)]
    cnt = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if graph[h][i][j] == 1:
                    q.append((h, i, j))
                    visited[h][i][j] = 1
                elif graph[h][i][j] == 0:
                    cnt += 1
    while q:
        ch, ci, cj = q.popleft()
        for dh, di, dj in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)):
            nh, ni, nj = ch+dh, ci+di, cj+dj
            if 0 <= nh < H and 0 <= ni < M and 0 <= nj < N and visited[h][i][j] == 0 and graph[h][i][j] == 0:
                q.append((nh, ni, nj))
                visited[nh][ni][nj] = visited[ch][ci][cj] + 1
                cnt -= 1
    if cnt == 0:
        return visited[ch][ci][cj]-1
    else:
        return -1


M, N, H = map(int, input().split())
graph = [[list(map(int, input().split()))] for _ in range(N) for _ in range(M)]
answer = bfs()
print()


# 1로 만들기

N = int(input())
dp = [0]*(N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    elif i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

ans = dp[N]
print(ans)
