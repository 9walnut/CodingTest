# 좌표 정렬하기 2
N = int(input())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort(key=lambda x: (x[1], x[0]))

for k in arr:
    x, y = k
    print(x, y)
