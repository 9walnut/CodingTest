# 가장 긴 바이토닉 부분 수열
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

dp1 = [1]*n
dp2 = [1]*n

sub_len = [0]*n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)

arr.reverse()

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

dp2.reverse()

for i in range(n):
    sub_len[i] = dp1[i] + dp2[i]

print(max(sub_len)-1)
