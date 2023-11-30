# 수들의 합
s = int(input())
n = 0
result = 0

for i in range(1, s+1):
    n += 1
    result += n
    if result > s:
        n -= 1
        break

print(n)
