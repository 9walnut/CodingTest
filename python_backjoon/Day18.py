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

#
