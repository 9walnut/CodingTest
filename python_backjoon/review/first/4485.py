# 녹색 옷 입은 애가 젤다지?\
# 다익스트라
import heapq
import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == n - 1 and y == n - 1:
            print(f'Problem {count}: {distance[x][y]}')
            break

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < n and 0 <= new_y < n:
                new_cost = cost + graph[new_x][new_y]

                if new_cost < distance[new_x][new_y]:
                    distance[new_x][new_y] = new_cost
                    heapq.heappush(q, (new_cost, new_x, new_y))


count = 1

while True:
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]

    dijkstra()
    count += 1


# BFS
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(i, j, graph, costs):
    queue = deque()
    queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if costs[nx][ny] > costs[x][y] + graph[nx][ny]:
                    costs[nx][ny] = costs[x][y] + graph[nx][ny]
                    queue.append((nx, ny))


count = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = []
    costs = [[int(1e9)] * n for _ in range(n)]
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    costs[0][0] = graph[0][0]
    bfs(0, 0, graph, costs)
    print(f'Problem {count}: {costs[n - 1][n - 1]}')
    count += 1
