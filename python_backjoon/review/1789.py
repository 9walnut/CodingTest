# 수들의 합
S = int(input())
N = 0
result = 0

for i in range(1, S+1):
    N += 1
    result += N
    if result > S:
        N -= 1
        break

print(N)
