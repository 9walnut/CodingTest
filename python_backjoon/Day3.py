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
