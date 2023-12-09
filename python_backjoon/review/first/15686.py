# 치킨 배달
# 치킨집과 집의 위치 리스트 저장
# 치킨집과의 최소값을 저장할 변수 지정
# m개수 만큼의 치킨집 골랐을 때 최소값을 찾아야하므로 m개의 치킨집을 고르는 조합의 수 구하기
# 조합의 수를 구하기 위해 브루트포스, 백트래킹 알고르짐
# dfs재귀를 반복하면서 조건 충족시 거리 저장
# 저장한 치킨집과의 거리를 min함수로 저장해 최솟값 출력

# n = 도시크기
# m = 치킨집수
import sys
from itertools import combinations
n, m = map(int, input().split())
graph = []
house = []
chicken = []

for col in range(n):
    graph.append(list(map(int, input().split())))
    for row in range(n):
        if graph[col][row] == 1:
            house.append((col, row))
        if graph[col][row] == 2:
            chicken.append((col, row))

# 백트래킹
arr = []
real_check = int(1e9)


def back(num, cnt):
    global real_check
    if num > len(chicken):
        return

    if cnt == m:
        result_tot = 0
        for hx, hy in house:
            min_check = int(1e9)
            for idx in arr:
                cx, cy = chicken[idx]
                min_check = min(min_check, abs(hx-cx)+abs(hy-cy))

            result_tot += min_check

        real_check = min(result_tot, real_check)
        return

    arr.append(num)
    back(num+1, cnt+1)
    arr.pop()
    back(num+1, cnt)
    return real_check


print(back(0, 0))


# 콤비네이션 활용 풀이
input = sys.stdin.readline

graph = []
# n = 도시의 정보, m = 치킨집 수
n, m = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 치킨집 좌표 저장
chicken = []
# 집 좌표 저장
house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i+1, j+1))
        elif graph[i][j] == 2:
            chicken.append((i+1, j+1))

result = n*2 * len(house)
for comb in list(combinations(chicken, m)):
    dist = 0
    for a, b in house:
        temp = n*2
        for x, y in comb:
            temp = min(temp, abs(a-x) + abs(b-y))
            dist += temp
    result = min(result, dist)

print(result)
