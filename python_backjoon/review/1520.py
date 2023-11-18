import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N = map(int, input().split())
dp = [[-1]*N for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(M)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def dfs(x, y):
    if x == M-1 and y == N-1:
        # 도착지점 도달시 한가지 경우의 수 리턴
        return 1
      # 이미 방문하였다면 그 위치에서 출발하는 경우를 리턴
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        newx = x + dx[i]
        newy = x + dy[i]
        if 0 <= newx < M and 0 <= newy < N:
          # 내리막길 인 경우 (이전길이 더 큰 경우)
            if arr[newx][newy] < arr[x][y]:
                dp[x][y] += dfs(newx, newy)
    return dp[x][y]


print(dfs(0, 0))
