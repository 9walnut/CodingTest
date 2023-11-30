# 내리막길
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
# 인덱스 오류 발생 m, n 범위 제대로 확인하고 지정.
dp = [[-1]*n for _ in range(m)]
arr = [list(map(int, input().split())) for _ in range(m)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0 <= newx < m and 0 <= newy < n:
            if arr[newx][newy] < arr[x][y]:
                dp[x][y] += dfs(newx, newy)
    return dp[x][y]


print(dfs(0, 0))
