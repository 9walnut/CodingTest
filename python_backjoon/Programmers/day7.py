# 게임 맵 최단거리
from collections import deque


def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            N = len(maps)
            M = len(maps[0])
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                answer = maps[N-1][M-1]
                if answer == 1:
                    answer -= 1
    return answer


def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            N = len(maps)
            M = len(maps[0])
            if 0 <= nx < N and 0 < ny <= M and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                answer = map[N-1][M-1]
                if answer == 1:
                    answer -= 1

    return answer


#  최소직사각형
def solution(sizes):
    # 1. 명함 지갑의 가로, 세로 길이 후보 list 변수 w, h 생성한다
    w = []  # 명함 지갑의 가로 길이 후보 리스트
    h = []  # 명함 지갑의 세로 길이 후보 리스트

    # 2. 주어진 명함들을 for 문을 돌면서 더 큰 값을 w, 작은 값을 h에 저장한다
    for size in sizes:
        if size[0] > size[1]:
            w.append(size[0])
            h.append(size[1])
        else:
            w.append(size[1])
            h.append(size[0])

    # 3. 각 w, h 리스트에서 가장 큰 값을 곱한다
    return max(w) * max(h)
