# 1992 쿼드트리
n = int(input())
board = [list(map(int, input())) for _ in range(n)]


def dfs(x, y, n):
    check = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != board[i][j]:
                check = -1
                break

    if check == -1:
      # 모두 같지 않으면 () 괄호 넣기
      # 처음엔 모두 같지 않기 때문에 () 넣고 시작
        print("(", end='')
        n = n//2
        # 여기 순서도 중요함
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
