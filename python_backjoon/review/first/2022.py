# 사다리
# 세 개의 숫자가 주어짐
# x, y, c인데 c에서 교차되고 x,y는 대각선 길이
# 빌딩간의 간격을 구하는 문제

from math import sqrt

x, y, c = map(float, input().split())
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
        strat = mid
    else:
        end = mid

print("{}".format(round(result, 4)))
