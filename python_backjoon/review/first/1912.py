# 연속합
n = int(input())
arr = list(map(int, input().split()))

dp = [0]*n
dp[0] = arr[0]
for i in range(1, n):
  # dp에 둘 중 최대값 저장(arr[i] : 음수가 있는 경우, dp[i-1]+arr[i] : 양수, +했을 시 커진 경우)
    dp[i] = max(arr[i], dp[i-1]+arr[i])
print(max(dp))
