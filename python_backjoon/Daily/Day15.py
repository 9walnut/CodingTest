# 백준 10757 - 큰수 A+B
import sys
a, b = map(int, input().split())

print(a+b)

# 2754 - 학점계산
t = str(input())

if t == "A+":
    print(4.3)
elif t == "A0":
    print(4.0)
elif t == "A-":
    print(3.7)
elif t == "B+":
    print(3.3)
elif t == "B0":
    print(3.0)
elif t == "B-":
    print(2.7)
elif t == "C+":
    print(2.3)
elif t == "C0":
    print(2.0)
elif t == "C-":
    print(1.7)
elif t == "D+":
    print(1.3)
elif t == "D0":
    print(1.0)
elif t == "D-":
    print(0.7)
elif t == "F":
    print(0.0)
