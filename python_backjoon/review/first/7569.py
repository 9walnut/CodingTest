# 토마토
from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    visit = [[0]*m for _ in range(n) for _ in range(h)]
    cnt = 0

    # 초기 데이터 삽입
    for H in range(h):
        for i in range(n):
            for j in range(m):
                if graph[H][i][j] == 1:
                    q.append((H, i, j))
                    visit[H][i][j] = 1
                else:
                    cnt += 1
    while q:
        ch, ci, cj = q.popleft()
        for dh, di, dj in ((0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)):
            nh, ni, nj = ch+dh, ci+di, cj+dj
            if 0 <= ni < n and 0 <= nj < m and 0 <= nh < h and visit[nh][ni][nj] == 0 and graph[nj][ni][nj] == 0:
                q.append((nh, ni, nj))
                visit[nh][ni][nj] = visit[ch][ci][cj] + 1
                cnt -= 1
    if cnt == 0:
        return visit[ch][ci][cj]-1
    else:
        return -1


m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
answer = bfs()
print(answer)
