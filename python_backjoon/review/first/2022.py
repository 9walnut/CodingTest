# 사다리
# 세 개의 숫자가 주어짐
# x, y, c인데 c에서 교차되고 x,y는 대각선 길이
# 빌딩간의 간격을 구하는 문제

from math import sqrt

x, y, c = map(float, input().split())
# 삼각혁의 특징상 대각선이 더 크기 때문에 그 특성을 이용해서 end는 x,y라는 대각선의 최소로 설정해서 이분탐색
start, end = 0, min(x, y)


def get_c(mid):
    a = sqrt(x**2-mid**2)
    b = sqrt(y**2-mid**2)
    return a*b/(a+b)


resutl = 0
while end-start > 1e-6:
    mid = (start+end)/2
    if get_c(mid) >= c:
        result = mid
        start = mid
    else:
        end = mid

print("{}".format(round(result, 4)))
