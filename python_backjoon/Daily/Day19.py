# 별찍기 1 - 2438
t = int(input())

for i in range(1, t+1):
    print("*"*i)

# 팩토리얼 - 10872
t = int(input())
result = 1
for i in range(1, t+1):
    if i <= t :
        result *=i
print(result)

def factorial(t):
    result = 1
    if n > 0:
        result = t*factorial(t-1)
    return result

# 피보나치 수 - 2747
t = int(input())
array = [0, 1]

for i in range(2, t+1):
    array.append(array[-1] + array[-2])
print(array[t])

# 피보나치 수 2747 - 다른풀이
 t = int(input())
 a, b = 0 , 1
 for i in range(t):
    a, b = b, a + b
print(a)

# 별찍기2 - 2439 
t= int(input())
for i in range(1, t+1):
    print(" "*(t-i) + "*"*i)

# 최대 공약수와 최소공배수 - 2609
a, b = map(int, input().split())

def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

def lcm(a, b):
    result = (a*b)//gcd(a, b)
    return result

print(gcd(a, b))
print(lcm(a, b))

t = int(input())
result = 0
for i in range(t+1):
    result += i
print(result)

result = 0
for i in range(5):
    result += int(input())
print(result)


import math

m = int(input())
n = int(input())
result = []

for i in range(m, n+1):
    if int(math.sqrt(i))**2 == i:
        result.append(i)

if result :
    print(sum(result))
    print(min(result))
else:
    print(-1)

t = int(input())

for i in range(1, t+1):
    print(t-i+1)

t = int(input())

for i in range(t):
    a = int(input())
    max_price = 0
    max_name = ""
    for _ in range(a):
        price, name = input().split()
        if int(price) > max_price:
            max_price = int(price)
            max_name = name
    print(max_name)

# 백준 5635 
t = int(input())
max_man = ""
max_age = 0
min_man = ""
min_age = float('inf')
for _ in range(t):
    a, b, c, d = input().split()
    age = int(b) + (int(c)*31) + (int(d)*31*365)
    if age > max_age:
        max_age = age
        max_man = a
    elif age < min_age:
        min_age = age
        min_man = a
print(max_man)
print(min_man)
# 다른 풀이
import sys
input = sys.stdin.readline

lst = []
for _ in range(int(input())):
    n,d,m,y = input().rstrip().split()
    d,m,y = map(int,(d,m,y))
    lst.append((y,m,d,n))
lst.sort()
print(lst[-1][3])
print(lst[0][3])