# 1차원 리스트
# N개의 원소가 0으로 초기화
L = [0] * n
# N개의 원소가 True
L = [True]*N
# 공백 기준 입력받기
n, m = map(int, input().split())

# 2차원 배열 선언(문자열 입력받아 그래프)
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# N*N 행렬을 0으로 초기화
board = [[0]*(N) for _ in range(N)]

# row*col행렬을 0으로 초기화
board2 = [[0]*(col) for _ in range(row)]

# 그래프 초기화
graph = [[] for i in range(n+1)]


# 유클리드 호제법
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# 최소공배수 구하기
# 위에서 구한 최대 공약수로 나눠주면 됨


def lcm(a, b):
    result = (a*b)//gcd(a, b)
    return result

import sys #한 줄에 여러 입력 값을 받는 함수
sys.stdin.readline().rstrip() : #오른쪽 공백 제거
sys.stdin.readline().lstrip() : #왼쪽 공백 제거
sys.stdin.readline().strip() : #좌우 공백 제거