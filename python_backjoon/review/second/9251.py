# LCS
import sys
input = sys.stdin.readline

string_a = ' ' + input().rstrip
string_b = ' ' + input().rstrip
dp = [[0] * len(string_b) for _ in range(len(string_a))]

for i in range(1, len(string_a)):
    for j in range(1, len(string_b)):
        if string_b[j] == string_a[i]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
