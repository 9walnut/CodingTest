# 특정 거리의 도시 찾기
from collections import deque
import sys
inpnt = sys.stdin.readline

# n : 도시 개수, m : 도로의 개수, k : 거리 정보, x : 출발도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [0]*(n+1)
visit = [False]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


# 일반적인 bfs와 달리 방문처리 후 해당위치에서 거리 +1
# 거리가 목표거리(K)와 같아질 경우 anwer 리스트에 넣은 후 오름차순, 프린트
def bfs(start):
    answer = []
    q = deque([start])
    visit[start] = True
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visit[i]:
                visit[i] = True
                q.append(i)
                distance[i] = distance[now]+1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        return (-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')


bfs(x)
