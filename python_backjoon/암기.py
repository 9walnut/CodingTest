# 공백 기준 입력받기
n, m = map(int, input().split())

# 2차원 배열 선언
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
