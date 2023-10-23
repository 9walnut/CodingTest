# 백준 최소 공배수 - 1934
# 유클리드 호제법
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return (gcd(b, a % b))


def lcm(a, b):
    result = (a*b) // gcd(a, b)
    return result


t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))

# 백준 개표 - 10102
t = int(input())
array = list(str(input()))
A_count = 0
B_count = 0

for i in array:
    if i == "A":
        A_count += 1
    elif i == "B":
        B_count += 1
if A_count > B_count:
    print("A")
elif B_count > A_count:
    print("B")
else:
    print("Tie")

# 백준 주사위 - 2480
a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a*1000)
elif a == b or a == c:
    print(1000 + a*100)
elif b == c:
    print(1000 + b*100)
elif a != b != c:
    print(max(a, b, c)*100)

# 배수와 약수 -5086
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    elif a > b and a % b == 0:
        print("multiple")
    elif a < b and b % a == 0:
        print("factor")
    else:
        print("neither")

# 약수들의 합  9506
while True:
    a = int(input())
    if a == -1:
        break
    array = []
    for i in range(1, a):
        if a % i == 0:
            array.append(i)
    if sum(array) == a:
        print(a, " = ", " + ".join(str(i) for i in array), sep="")
    else:
        print(a, "is NOT perfect.")
