# 좌표 정렬하기 2
n = int(input())
arr = []
for _ in range(n):
    xy = list(map(int, input().split()))
    arr.append(xy[1], xy[0])

arr.sort()

for i in arr:
    print(i[1], [0])

# 다른 풀이
n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append([y, x])

s_arr = sorted(arr)

for y, x in s_arr:
    print(x, y)

# 다른 풀이
coord_list = []
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    coord_list.append((x, y))

coord_list.sort(key=lambda x: (x[1], x[0]))

for coord in coord_list:
    x, y = coord
    print(x, y)
