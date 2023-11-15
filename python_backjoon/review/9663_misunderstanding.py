# N-Queen

# 퀸이 서로 공격할 수 없도록 하는 방법
# 같은 행 X, 같은 열 X, 대각선 X

# 대부분 백트래킹 문제는 dfs와  promising을 선언하여 문제풀이함
import sys
n = int(sys.stdin.readline().rstrip())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
      # 같은 위치 or 대각선 검증
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
  global ans
  
  if x == n:
      ans += 1
    
  else :
    for i in range(n):
      row[x] = i
      if is_promising(x):
        n_queens(x+1)

n_queens(0)
print(ans)