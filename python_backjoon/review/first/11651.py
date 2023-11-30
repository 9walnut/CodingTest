# 좌표 정렬하기 2

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

# 좌표 (x,y)에 대해 (y,x)로 순서쌍 반환
coord_list.sort(key=lambda x: (x[1], x[0]))

for coord in coord_list:
    x, y = coord
    print(x, y)
