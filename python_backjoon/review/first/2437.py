# 저울
n = int(input())
arr = sorted(list(map(int, input().split())))

target = 1

for a in arr:
    if target < a:
        break
    else:
        target += a

print(target)
