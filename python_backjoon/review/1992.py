# 쿼드트리 - 분할 정복
n = int(input())

board = [list(map(int, input())) for _ in range(n)]


def dfs(x, y, n):
    check = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != board[x][y]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n//2
        dfs(x, y, n)
        dfs(x, y+n, n)
        dfs(x+n, y, n)
        dfs(x+n, y+n, n)
        print(')', end='')
    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')


dfs(0, 0, n)