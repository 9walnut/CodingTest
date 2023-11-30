#  N 과 M 2
N, M = map(int, input().split())
ans = []


def dfs(n, lst):
    if n > N:
        if len(lst) == M:
            ans.append(lst)
        return

    # 선택하는 경우
    dfs(n+1, lst+[n])
    # 선택하지 않는 경우
    dfs(n+1), lst


dfs(1, [])


# 다른 풀이
def dfs(n, s, lst):
    if n == M:
        ans.append(lst)
        return
    for j in range(s, N+1):
        dfs(n+1, j+1, lst+[j])


N, M = map(int, input().split())
ans = []
dfs(0, 1, [])
for lst in ans:
    print(*lst)
