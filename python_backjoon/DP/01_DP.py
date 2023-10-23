# 2747 - 피보나치 수
# 시작적으로 접근
# DP 테이블 정의
# 초기값 설정, 반복

N = int(input())
dp = [0]*(N+1)
dp[1] = 1

for i in range(2, N+1):
    dp[i] = dp[i-2] + dp[i-1]


ans = dp[N]
print(ans)

# 1로 만들기 - 1463

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

# 11727  - n타일링
N = int(input())
dp = [0]*(N+1)
dp[1], dp[2] = 1, 3

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]*2

ans = dp[N]
print(ans % 10007)
