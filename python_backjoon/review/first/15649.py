# N과 M
n, m = list(map(int, input().split()))

s = []


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()


# 다른 풀이
N, M = map(int, input().split())
ans = []
v = [0]*(N+1)  # 중복 확인을 위한 배열


def dfs(n, lst):
    # 종료 조건 (n)에 관한 조건이어야함
    if n == M:
        ans.append(lst)
        return

    # 하부단계 호출
    for j in range(1, N+1):  # 1부터 N 까지
        if v[j] == 0:  # 미 방문 숫자 인 경우
            v[j] = 1  # 방문 처리
            dfs((n+1), lst+[j])
            v[j] = 0


dfs(0, [])
for lst in ans:
    print(*lst)
