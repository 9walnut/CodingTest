#  토마토
from collections import deque

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split()))] for _ in range(N) for _ in range(M)]
answer = bfs()
print()


def bfs():
    q = deque()
