# 백준 1789 - 수들의 합
S = int(input())
N = 0
result = 0

for i in range(1, S+1):
    N += 1
    result += N
    if (result > S):
        N -= 1
        break
print(N)

# 백준 2753 - 윤년
n = int(input())

if ((n % 4 == 0) and (n % 100 != 0)) or (n % 400 == 0):
    print('1')
else:
    print('0')

# 백준 10039 - 평균 점수
result = 0
for i in range(5):
    score = int(input())
    if score < 40:
        result += 40
    else:
        result += score

print(int(result/5))

# 백준 10103 - 주사위
n = int(input())
C = 100
S = 100

for i in range(1, n+1):
    a, b = map(int, input().split())
    if a > b:
        S -= a
    elif a < b:
        C -= b

print(C)
print(S)

# 백준 5717 - 상근이의 친구들
# 이거 왜 전역 변수면 시간 초과 나는지?

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a+b)
