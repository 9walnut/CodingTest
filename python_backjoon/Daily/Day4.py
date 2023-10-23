# 백준 3009 - 네번째 점
a_points = []
b_points = []

for _ in range(3):
    a, b = map(int, input().split())
    a_points.append(a)
    b_points.append(b)

for i in range(3):
    if a_points.count(a_points[i]) == 1:
        a4 = a_points[i]
    if b_points.count(b_points[i]) == 1:
        b4 = b_points[i]

print(a4, b4)

# 백준 11557 - 양조장의 해
t = int(input())
for _ in range(t):
    N = int(input())
    maxliter = 0
    maxUniv = ""
    for i in range(N):
        univ, liter = input().split()
        liter = int(liter)
        if (liter > maxliter):
            maxliter = liter
            maxUniv = univ
    print(maxUniv)

# 백준 7567 - 그릇
dish = input()
answer = 10

for i in range(1, len(dish)):
    if dish[i] == dish[i-1]:
        answer += 5
    else:
        answer += 10

print(answer)

# 백준 5063 - TGN
t = int(input())

for _ in range(t):
    r, e, c = map(int, input().split())
    if r > e-c:
        print("do not advertise")
    elif r < e-c:
        print("advertise")
    else:
        print("does not matter")
