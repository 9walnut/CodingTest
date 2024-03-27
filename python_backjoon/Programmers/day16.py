import sys

# 1260 DFS와 BFS

# DFS
# 방문 표시
# ans_dfs.append(c)


def dfs(c):
    ans_dfs.append(c)  # 방문 노드 추가
    v[c] = 1  # 방문 표시

    for n in adj[c]:
        if not v[n]:
            dfs(n)


def bfs(s):
    q = []
    q.append(s)  # 초기데이터 삽입
    ans_bfs.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not v[n]:  # 방문하지 않은 노드 => 큐 삽입
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1


# 다음 노드 방문
# for n in adj[c]
#  if v[n] == 0: dfs(n)
N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

# 오름 차순 정렬
for i in range(1, N+1):
    adj[i].sort()

v = [0]*(N+1)
ans_dfs = []
dfs(V)

v = [0]*(N+1)
ans_bfs = []
bfs(V)


print(*ans_dfs)
print(*ans_bfs)
# BFS(s)
# 1. q, v, 변수 생성
# 2. q에 초기데이터들을 삽입 v[] 표시, ans 처리
# while q:
#  q에서 데이터 한개 꺼냄
#  for 네 방향, 8 방향...등 반복 / 조건에 맞으면 q에 삽입
# 문제가 바뀌면 조건 부분이 바뀌는 것임

# 미로 탐색
