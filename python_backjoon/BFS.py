# 16173 - 점프왕 젤리
from collections import deque
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 방문 유무 확인
visited = [[False]*N for _ in range(N)]

# 오른쪽만 가능
dx = [1, 0]
# 아래만 가능
dy = [0, 1]


def bfs(x, y):
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        # 밟고 있는 칸의 숫자 인출
        step = graph[x][y]

        # 끝점이 -1이므로 -1로 도달하면 성공
        if graph[x][y] == -1:
            return True
        for move in range(2):
            # 밟고 있는 숫자를 인출해서 이동수에 곱해서 이동
            nx = x+dx[move]*step
            ny = y+dy[move]*step
        # 주어진 범위 벗어나는 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 방문하지 않았을 경우 방문 수정
            if not visited[nx][ny]:
                visited[nx][ny] = True
                # q에 담아주면서 반복
                q.append([nx, ny])


if bfs(0, 0):
    print('HaruHaru')
else:
    print("Hing")


# 바이러스 bfs


t = int(input())
link = int(input())
graph = [[] for i in range(t+1)]
visited = [0]*(t+1)
# 카운트?
cnt = 0

for i in range(link):
    a, b = map(int, input().split())
    graph[a].append[b]
    graph[b].append[a]


def bfs(graph, link):
    global cnt
    queue = deque[link]

    while queue:
        pop = queue.popleft()
        visited[pop] = True

        for i in graph[pop]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                cnt += 1
    print(cnt)


bfs(graph, 1)
