# 올바른 배열
n = int(input())

arr = [int(input() for _ in range(n))]
arr = sorted(arr)
temp = []

for i in range(0, n):
    cnt = 0
    for j in range(arr[i], arr[i]+5):
        if j not in arr:
            cnt += 1
    temp.append(cnt)
print(min(temp))
