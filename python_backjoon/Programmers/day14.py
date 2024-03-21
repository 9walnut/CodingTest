# DFS / BFS 네트워크
from collections import deque
# BFS


def solution(n, computers):
    computers = deque(computers)
    network = 0
    global visited
    visited = [False] * n

    for k in range(n):
        if BFS(n, computers, k, visited) == True:
            network += 1
    return network


def BFS(n, computers, k, visited):
    if visited[k] == True:
        return False

    queue = deque([computers[k]])
    visited[k] = True

    while len(queue) > 0:
        node = queue.popleft()
        for i in range(n):
            if i != k and node[i] == 1:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(computers[i])

    return True

# DFS 풀이


def solution(n, computers):
    network = 0
    visited = [False] * n  # 컴퓨터 갯수만큼
    for num in range(n):  # 각 컴퓨터 돌면서 방문안했으면 DFS 실행
        if visited[num] == False:
            DFS(n, computers, num, visited)
            network += 1  # 연결된 하나의 네트워크 +1
    return network


def DFS(n, computers, num, visited):
    visited[num] = True  # 방문 처리
    for cnt in range(n):  # 컴퓨터 갯수 만큼 반복
        # 자기 자신과의 연결 제외 and 컴퓨터가 서로 연결되어있다면 (문제 조건에서 숫자 1이면 연결)
        if num != cnt and computers[num][cnt] == 1:  # 자기 자신이 연결
            if visited[cnt] == False:  # 미방문
                DFS(n, computers, cnt, visited)
