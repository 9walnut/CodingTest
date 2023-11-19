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


sqrt : 제곱근 구하기

정수, 문자열시 입력값 받기
a, b = intput().split()

def backtrack(candidate):
	# 만약 현재 후보군이 유효한 해라면 정답 처리하고 backtrack 함수를 종료
    if find_solution(candidate):
        output(candidate)
        return
    
    # 반복문을 돌면서 가능한 모든 후보군에 대해 탐색
    for next_candidate in list_of_candidates:
    	# 유효한 후보군인 경우에만 탐색 진행
        if is_valid(next_candidate):
            # 이 후보군을 우선 추가하고,
            place(next_candidate)
            # 후보군을 추가한 상태에서 다음 후보군에 대해서 탐색 진행
            backtrack(next_candidate)
            # 해당 후보군에 대한 탐색을 종료한 이후에는 제거
            remove(next_candidate)
            
            
# CCW 알고리즘
def ccw(p1, p2, p3):
    A = p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]
    B = p1[1]*p2[0] + p2[1]*p3[1] + p3[1]*p1[0]
    if A-B == 0:
        return 0
    elif A-B > 0:
        return 1
    else:
        return -1


P1 = list(map(int, input().split()))
P2 = list(map(int, input().split()))
P3 = list(map(int, input().split()))
print(ccw(P1, P2, P3))