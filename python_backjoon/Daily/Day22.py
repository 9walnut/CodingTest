#  별찍기 8 - 2445
import sys
t = int(input())

for i in range(1, 2*t):
    if i <= t:
        print("*"*i + " "*(2*t-2*i) + "*"*i)
    else:
        print("*"*(2*t-i)+" "*(2*i-2*t)+"*"*(2*t-i))

#  얼마? 9325
t = int(input())
for _ in range(t):
    price = int(input())
    option_count = int(input())
    total_price = price

    for _ in range(option_count):
        q, p = map(int, input().split())
        option_price = q*p
        total_price += option_price
    print(total_price)

# 플러그 - 2010
input = sys.stdin.readline

mt = int(input())
total = 0
for _ in range(mt):
    total += int(input())
print(total - (mt - 1))

# 할로윈 10178
t = int(input())
for _ in range(t):
    c, v = map(int, input().split())

print("You get {:d} piece(s) and your dad gets {:d} piece(s).".format(
    c//v, c % v))

for _ in range(int(input())):
    c, v = map(int, input().split())
    print(f"You get {c//v} piece(s) and your dad gets {c % v} piece(s).")

# 주사위 - 9295
t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f"Case {i}: {a+b}")

t = int(input())
for i in range(1, t + 1):
    a, b = map(int, input().split())
    print("Case ", i, ": ", a + b, sep='')
