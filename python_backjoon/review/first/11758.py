# 내가 푼 쓰레기같은 코드 ㅋㅋㅋ
# 첫번째 테스트케이스만 유효했음...
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

for _ in range(3):
    if x1 < x2 and y1 < y2 and y2 > y3 and x2 > x3:
        print(1)
        break
    elif x1 == y1 and x2 == y2 and x3 == y3:
        print(0)
        break
    else:
        print(-1)
        break

# ccw 알고리즘을 알아서 풀수 있는 문제


def ccw(p1, p2, p3):
    A = p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]
    B = p1[1]*p2[0] + p2[1]*p3[0] + p3[1]*p1[0]
    if A-B == 0:  # 일직선
        return 0
    elif A-B > 0:  # 반시계
        return 1
    else:  # 시계
        return -1


P1 = list(map(int, input().split()))
P2 = list(map(int, input().split()))
P3 = list(map(int, input().split()))
print(ccw(P1, P2, P3))
