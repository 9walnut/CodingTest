# 스택 수열
import sys
input = sys.stdin.readlines

n = int(input())
list = []
for i in range(n):
    a = int(input)
    if i < a:
        print("+")
    else:
        print("-")
