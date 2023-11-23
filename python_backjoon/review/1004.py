# 어린 왕자
t = int(input())

for _ in range(t):
    # 출발점, 도착점 입력
    x1, y1, x2, y2 = list(map(int, input().split()))
    n = int(input())
    count = 0
    # 각 행성 좌표, 반지름 입력
    for _ in range(n):
        cx, cy, cr = map(int, input().split())

        dis1 = (x1 - cx)**2 + (y1-cy)**2
        dis2 = (x2 - cx)**2 + (y2-cy)**2
    # 각 행성의 반지름
        pow_cr = cr**2

    # 행성의 반지름이 더 긴 경우 이탈/진입 없음
        if pow_cr > dis1 and pow_cr > dis2:
            pass
    # 하나만 큰 경우
        elif pow_cr > dis1:
            count += 1
    # 하나만 큰 경우
        elif pow_cr > dis2:
            count += 1
    print(count)
