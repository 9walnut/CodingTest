# 11048 - 이동하기
N, M = map(int, input().split())
arr = [[0]*(M+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        # 세 좌료부로터의 누적값 최대치 + i,j 에서 더한 사탕 수
        dp[i][j] = arr[i][j] + max(dp[i-1][j], dp[i][j-1], dp[i-1[j-1]])

print(dp[N][M])

# 1890 - 점프
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0*N for _ in range(N)]
dp[0][0] = 1

# 갱신 전체 순회
for i in range(N):
    for j in range(N):
        # 경로가 있고, 점프 숫자가 있는 경우
        if dp[i][j] > 0 and arr[i][j] >0:
            jump = arr[i][j]
            if j+jump< N: #우측 범위내인 겨우
                dp[i][j+jump] += dp[i][j]
            if i+jump< N: #아래쪽 범위내인 겨우
                dp[i+jump][j] += dp[i][j]

print(dp[N-1][M-1])

# 1520 - 내리막길

def dfs(ci, cj):
    if dp[ci][cj] == -1: #계산이 안된경우
        dp[ci][cj] = 0
        for di, dj in ((-1, 0),(1,0), (0,-1), (0,1)):
            pi, pj = ci+di, cj+dj # 이전 좌표 계산
            if arr[pi][pj]> arr[ci][cj] : # 내리막인 경우
                dp[ci][cj]+=dfs(pi,pj) #조건에 맞는 4방햐 누적
    return dp[ci][cj]
            
N, M = map(int, input().split())
# 범위 체크 생략을 위해 0으로 둘러쌓기
arr = [[0]*(M+2)] + [[[0]*(M+2) list(map(int, input().split())) + [0]*(M+2)]
# dp테이블 생성 및 초기값 설정
dp = [[-1]*(M+2) for _ in range(N+2)]
dp[1][1] = 1




print(dfs(N, M))
