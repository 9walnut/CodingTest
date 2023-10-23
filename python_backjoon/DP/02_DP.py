#  11057 - 오르막수
#  2차원 풀이
N = int(input())

dp = [[0]*10 for _ in range(N+1)]
dp[1] = [1]*10

for i in range(2, N+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:])

ans = sum(dp[N])
print(ans % 10007)

# 다른 풀이 1차원

N = int(input())

dp = [1]*10

for i in range(2, N+1):
    for j in range(10):
        dp[j] = sum(dp[j:])

ans = sum(dp)
print(ans % 10007)

# 또 다른 풀이
N = int(input())
dp = [1]*10

for _ in range(N-1):
    for j in range(1, 10):
        dp[j] = dp[j] + dp[j-1]

ans = sum(dp)
print(ans % 10007)

#  10844 쉬운 계단수
N = int(input())
dp = [[0]*12 for _ in range(N+1)]
dp[1][2:11] = [1]*9

for i in range(2, N+1):
    for j in range(1, 11):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

ans = sum(dp[N])
print(ans % 1000000000)
