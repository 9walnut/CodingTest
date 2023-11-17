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
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        newx = x + dx[i]
        newy = x + dy[i]
        if 0 <= newx < M and 0 <= newy < N:
            if arr[newx][newy] < arr[x][y]:
                dp[x][y] += dfs(newx, newy)
    return dp[x][y]


print(dfs(0, 0))
