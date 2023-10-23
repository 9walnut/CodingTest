# 영수증 5565
t = int(input())
x = 0

for _ in range(9):
    x -= int(input())

print(x)

# A+B-3
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(a+b)

#  A+B-5

while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a+b)

# 내 학점을 구해줘
T = int(input())

for _ in range(T):
    N = int(input())
    total_credit = 0
    total_grade = 0

    for _ in range(N):
        credit, grade = map(float, input().split())
        total_credit += credit
        total_grade += grade*credit
    GPA = total_grade / total_credit
    print(int(total_credit), '%.1f' % GPA)

# 사과
t = int(input())
list = []
for _ in range(t):
    a, b = map(int, input().split())
    result = b % a
    list.append(result)
print(sum(list))

# 별찍기12
t = int(input())
for i in range(1, 2*t):
    if i <= t:
        print(" "*(t-i) + "*"*i)
    else:
        print(" "*(i-t) + "*"*(2*t-i))

# 별찍기 13
t = int(input())
for i in range(1, 2*t):
    if i <= t:
        print("*"*(i))
    else:
        print("*"*(2*t-i))
