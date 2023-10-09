#  백준 2606 - 바이러스

computer = int(input())
link = int(input())  # 연결선 개수
# 그래프 초기화
# n+1인 이유는 1번 인덱스에 1번 컴퓨터를 삽입하기 위함
graph = [[] for i in range(computer+1)]
# 방문한 컴퓨터인지 표시
visited = [0]*(computer+1)

# 그래프 생성
for i in range(link):
    a, b = map(int, input().split())
    # 연결된 컴퓨터 번호를 각각 a,b입력 받고 쌍방으로 기입함으로써 연결
    graph[a] += [b]
    graph[b] += [a]


def dfs(link):
    visited[link] = 1
    # grapgh[link]는 link번 컴퓨터에 연결된 리스트
    for nx in graph[link]:
        if visited[nx] == 0:
            dfs(nx)


dfs(1)
# 1번 컴퓨터를 제외하기 때문에 -1
print(sum(visited)-1)

# 백준 1388 - 바닥장식


def dfs(x, y):
    # 바닥이 "-"일때
    if graph[x][y] == '-':
        graph[x][y] = 1
        for _y in [1, -1]:  # 양 옆 확인
            Y = y + _y
            if (Y > 0 and Y < m) and graph[x][Y] == '-':
                dfs(x, Y)

    if graph[x][y] == '|':
        graph[x][y] = 1
        for _x in [1, -1]:  # 상하 확인
            X = x + _x
            if (X > 0 and X < n) and graph[X][y] == '|':
                dfs(X, y)


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '-' or graph[i][j] == '|':
            dfs(i, j)
            count += 1
print(count)

# 백준 16173 - 점프왕 쩰리

def dfs(x, y):
    # 범위 벗어나면 0 처리
    if x >= t or x <= -1 or y >= t or y <= -1 or visited[x][y] == 1:
        return
    if graph[x][y] == -1:
        visited[x][y] =1
        return
    visited[x][y]=1

    # 상하좌우 요소 수만큼 점프 이동
    dfs(x+graph[x][y],y) #상,하
    dfs(x, y+graph[x][y]) #좌,우

t= int(input())
# graph = []
# for _ in range(t):
#     graph.append(list(map(int, input().split())))
graph=[list(map(int, input().split())) for _ in range(t)]

visited = [[0]*t for _ in range(t)]

# 출발지 0,0 호출
dfs(0, 0)
# 결과 출력
if visited[-1][-1] == 1:
    print("HaruHaru")
else:
    print("Hing")
