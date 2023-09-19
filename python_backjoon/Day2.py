# 백준 2935 - 소음
import math
a = int(input())
b = input()
c = int(input())

if (b == '*'):
    print(a*c)
else:
    print(a+c)


# 백준 9498 - 시험 성적
a = int(input())
if (a >= 90):
    print('A')
elif (a >= 80):
    print('B')
elif (a >= 70):
    print('C')
elif (a >= 60):
    print('D')
else:
    print('F')

# 백준 10817 - 세 수
num_list = list(map(int, input().split()))
num_list.sort()
print(num_list[1])

# 백준 11653 - 소인수분해
# 하기 코드는 공간출력도가 높음
a = int(input())
b = 2
while a != 1:
    if a % b == 0:
        print(b)
        a = a//b
    else:
        b += 1

# 타인 코드 참고

N = int(input())    # 나누어지는 수
d = 2               # 나누는 수
sqrt = int(math.sqrt(N))  # 나누어지는 수의 제곱근

# 나누는 수가 제곱근이하인 동안
while d <= sqrt:
    if N % d != 0:  # 나누어 떨어지지 않으면
        d += 1      # 나누는 수 1 증가
    else:           # 나누어 떨어지면
        print(d)    # 소인수니까 출력하고
        N //= d     # 나누어지는 수도 갱신

# 제곱근까지 나누어떨어지지 않으면, 소수이므로 그대로 출력
if N > 1:
    print(N)
