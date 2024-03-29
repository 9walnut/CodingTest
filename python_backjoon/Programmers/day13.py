import heapq
from collections import deque


def solution(jobs):
    answer, now, i = 0
    start = -1
    heap = []

    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])

            if heap:
                current = heapq.heappop(heap)
                start = now
                now += current[0]
                answer += now - current[1]
                i += 1
            else:
                now += 1

    return answer // len(jobs)


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


def solution(n, conmputers):
    network = 0
    visited = [False] * n
    for num in range(n):
        if visited[num] == False:
            DFS(n, conmputers, num, visited)
            network += 1
    return network


def DFS(n, computers, num, visited):
    visited[num] = True
    for cnt in range(n):
        if num != cnt and computers[num][cnt] == 1:
            if visited[cnt] == False:
                DFS(n, computers, cnt, visited)
