#  피보나치 수
n = int(input())
dp = [0]*(n+1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
ans = dp[n]
print(ans)

# 1로 만들기 -1463
N = int(input())
dp = [0]*(N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1]+1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    elif i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[N])
