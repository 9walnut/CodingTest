#  다면체 - 10569
t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    result = 2 - v + e
    print(result)

# 별찍기 20
t = int(input())
for i in range(t):
    if i % 2 == 0:
        print(("* ")*(t))
    elif i % 2 != 0:
        print((" *")*(t))

# 도미노
t = int(input())
sum = 0
for i in range(t+1):
    for j in range(i+1):
        sum += (i + j)
print(sum)

#  별찍기 16
t = int(input())
for i in range(t):
    print(" "*(t-i-1) + "* "*(i+1))

# X보다 작은 수
N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")
