# 가장 긴 증가하는 수열
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# dp = [1]*n

# for i in range(n):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j]+1)

# print(max(dp))

dp = []
dp.append(arr[0])
for i in range(1, n):
    if dp[len(dp)-1] < arr[i]:
        dp.append(arr[i])

print(len(dp))
