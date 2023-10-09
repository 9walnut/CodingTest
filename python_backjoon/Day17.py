# 백준 9610 - 사분면
t = int(input())
Q1 = Q2 = Q3 = Q4 = AXIS = 0

for i in range(t):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        Q1 += 1
    elif x < 0 and y > 0:
        Q2 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    elif x > 0 and y < 0:
        Q4 += 1
    elif x == 0 or y == 0:
        AXIS += 1
print("Q1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)
print("Q4:", Q4)
print("AXIS:", AXIS)

# 백준 2884 - 알람시계
a, b = map(int, input().split())
# 분 단위로 변환
time = a*60 + b - 45
a_reset = time//60
b_reset = time % 60
if a == 0 and b < 45:
    print(f'23 {b_reset}')
else:
    print(f'{a_reset} {b_reset}')
