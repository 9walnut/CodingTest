from collections import deque

t = int(input())
link = int(input())
graph = [[] for _ in range(t+1)]
visit = [0]*(t+1)
cnt = 0

for i in range(link):
    a, b = map(int, input().split())
    graph[a].append[b]
    graph[a].append[b]


def bfs(graph, link):
    global cnt
    queue = deque[link]
    while queue:
        pop = queue.popleft()
        visit[pop] = True

        for i in graph[pop]:
            if visit[i] == 0:
                visit[i] = 1
                queue.append(i)
                cnt += 1
    print(cnt)
