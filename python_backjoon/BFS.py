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

# 촌수계산

t = int(input())
a, b = map(int, input().split())
link = int(input())
visited = [0]*(t+1)
graph = [[] for i in range(t+1)]
result = -1

for i in range(link):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(start):
    q = deque()
    q.append((start, 0))
    visited[start] = 1

    while q:
        node, depth = q.popleft()

        if node == b:
            return depth

        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                q.append((i, depth+1))


result = bfs(a)

if result is not None:
    print(result)
else:
    print(-1)

# 단지번호붙이기


def bfs(si, sj):
    q = []
    q.append((si, sj))  # 큐 초기 데이터 삽입
    visited[si][sj] = 1  # 방문표시
    cnt = 1  # 정답처리

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < t and 0 <= nj < t and visited[ni][nj] == 0 and graph[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] = 1
                cnt += 1
    return cnt


t = int(input())
# 잘못기입받았음
graph = [list(map(int, input())) for i in range(t)]
visited = [[0]*t for i in range(t)]
ans = []

for i in range(t):
    for j in range(t):
        if graph[i][j] == 1 and visited[i][j] == 0:
            ans.append(bfs(i, j))

ans.sort()
# 출력형식
print(len(ans), *ans, sep='\n')
