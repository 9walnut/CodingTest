# 파이프 옮기기 1
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

HO = 0  # 가로
VIR = 1  # 세로
DIAG = 2  # 대각
cnt = 0


def dfs(nowy, nowx, type):
    global cnt
    if (nowy, nowx) == (n-1, n-1):
        cnt += 1
        return

    if type == HO or type == DIAG:
        if nowx+1 < n and board[nowy][nowx+1] == 0:
            dfs(nowy, nowx+1, HO)
    if type == VIR or type == DIAG:
        if nowy + 1 < n and board[nowy+1][nowx] == 0:
            dfs(nowy+1, nowx, VIR)

    if nowx+1 < n and nowy+1 < n:
        if board[nowy+1][nowx] == 0 and board[nowy][nowx+1] == 0 and board[nowy+1][nowx+1] == 0:
            dfs(nowy+1, nowx+1, DIAG)


dfs(0, 1, HO)
print(cnt)


# dp

def solution():

    # 1행 미리 처리하기 → (3) 과정
    dp[0][0][1] = 1
    for i in range(2, N):
        if board[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]

    # 왜 1행과 1열을 제외하는지는 (3), (4) 과정에서 봤었죠?
    for r in range(1, N):
        for c in range(1, N):
            # (5) 과정
            # 대각선 파이프를 추가하는 과정
            if board[r][c] == 0 and board[r][c - 1] == 0 and board[r - 1][c] == 0:
                dp[1][r][c] = dp[0][r - 1][c - 1] + \
                    dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

            # 가로, 세로 파이프를 추가하는 과정
            if board[r][c] == 0:
                dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
                dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]

    # 최종 결과 출력
    print(sum(dp[i][N - 1][N - 1] for i in range(3)))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
solution()
