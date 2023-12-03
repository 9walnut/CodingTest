# 어두운 굴다리
# 굴다리 길이 n
import sys
n = int(input())
# 가로등 개수 m
m = int(input())
# 가로등 위치 x
position = list[map(int, input().split())]
len_position = len(position)

# 가로등이 하나 있는 경우
if len_position == 1:
    min_height = max(position[0]-0, n-position[0])

# 가로등이 하나 이상인 경우
else:
    for i in range(len_position):
        if i == 0:
            height = position[i] - 0
        elif i == len_position[i] - 1:
            height = n - position[i]
        else:
            tmp = position[i] - position[i-1]
            if tmp % 2:
                height = tmp//2+1
            else:
                height = tmp//2
        min_height = max(height, min_height)

print(min_height)


# 다른 풀이
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = list(map(int, input().split()))

max_size = 0
for i in range(1, M):
    max_size = max(max_size, arr[i] - arr[i-1])

# 가장 가까운 두 개의 좌표상의 거리
# 첫 좌표와 원점사이의 거리
# 마지막 좌표와 원점 사이의 거리
print(max((max_size+1)//2, arr[0] - 0, N - arr[-1]))

# 이분탐색


def bs(li, m):
    if li[1]-li[0] > m:
        return 0
    if li[-1]-li[-2] > m:
        return 0
    for i in range(1, len(li)-2):
        if (li[i+1]-li[i])/2 > m:
            return 0
    return 1


N, M = int(input()), int(input())
li = [0] + list(map(int, input().split())) + [N]
s, e = 0, N
res = 0
while s <= e:
    m = (s+e)//2
    if bs(li, m):
        e = m-1
        res = m
    else:
        s = m+1
print(res)
