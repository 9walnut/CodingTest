# 백준 -2476 주사위게임
t = int(input())
result = 0
array = []

for i in range(t):
    a, b, c = map(int, input().split())
    if a == b == c:
        result = 10000 + (a*1000)
    elif a == c or a == b:
        result = 1000 + (a*100)
    elif b == c:
        result = 1000 + (b*100)
    else:
        result = max(a, b, c)*100
    array.append(result)
print(max(array))

# 10156 - 과자
# 과자 한개 k, 과자 개수 n, 가진돈 m
# 모자란돈 (k*n) - m

k, n, m = map(int, input().split())
result = 0

if k*n-m > 0:
    result = k*n - m
    print(result)
else:
    print(0)

# 4101 - 크냐?
while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    elif a <= b:
        print("No")
    else:
        print("Yes")

# 10214 - Baseball
t = int(input())

for _ in range(t):
    a_result = 0
    b_result = 0
    for i in range(9):
        a, b = map(int, input().split())
        a_result += a
        b_result += b
    if a_result > b_result:
        print("Yonsei")
    elif a_result < b_result:
        print("Korea")
    else:
        print("Draw")
