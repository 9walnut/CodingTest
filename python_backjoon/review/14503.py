# 로봇 청소기
# N M크기의 직사각형 방
# (0, 0) ~(N-1, M-1) 범위
# 현재 칸의 4칸 중 청소되지 않은 빈칸 없는 경우
# 후진 가능, 후진하려는 칸이 벽이면 작동 멈춤
# 빈칸 있는 경우 90도 회전

#  d -- 북,서,남,동 순으로 (반시계 방향 회전)
n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
visited = [[0]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

visited[r][c] = 1
cnt = 1

while 1:
    flag = 0
    for _ in range(4):
        # 북, 서, 남, 동 순서 만들어주기 위한 식
        d = (d+3) % 4
        nx = r + dx[d]
        ny = c + dy[d]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny
                flag = 1
                break
    if flag == 0:
        if graph[r-dx[d]][c-dy[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r-dx[d], c-dy[d]
