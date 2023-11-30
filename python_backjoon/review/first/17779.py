# 게리맨더링2
def cal(x, y, d1, d2):
    elec = [0 for _ in range(5)]  # 선거구 당 인구수
    temp = [[0]*(n+1) for _ in range(n+1)]  # 선거국

    # 경계선을 5번 선거구로 할당
    for i in range(d1+1):
        temp[x+i][y-i] = 5  # 1번조건
        temp[x+d2+i][y+d2-i] = 5  # 3번 조건
    for i in range(d2+1):
        temp[x+i][y+i] = 5  # 2번 조건
        temp[x+d1+i][y-d1+i] = 5  # 4번 조건
    # 경계선 내부를 5번 선거구로 할당
    for i in range(x+1, x+d1+d2):
        flag = False
        for j in range(1, n+1):
            if temp[i][j] == 5:
                flag = not flag
            if flag:
                temp[i][j] = 5

    # 각 선거구
    for r in range(1, n+1):
        for c in range(1, n+1):
            if r < x+d1 and c <= y and temp[r][c] == 0:
                elec[0] += graph[r][c]
            elif r <= x+d2 and y < c and temp[r][c] == 0:
                elec[1] += graph[r][c]
            elif x+d1 <= r and c < y-d1+d2 and temp[r][c] == 0:
                elec[2] += graph[r][c]
            elif x+d2 < r and y-d1+d2 <= c and temp[r][c] == 0:
                elec[3] += graph[r][c]
            elif temp[r][c] == 5:
                elec[4] += graph[r][c]
    return max(elec) - min(elec)


n = int(input())
graph = [[]]
result = 1e9
for i in range(n):
    graph.append([0]+list(map(int, input().split())))

# 완전 탐색
for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if 1 <= x < x+d1+d2 <= n and 1 <= y-d1 < y < y+d2 <= n:
                    result = min(result, cal(x, y, d1, d2))

print(result)
