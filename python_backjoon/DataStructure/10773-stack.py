# 제로
import sys
input = sys.stdin.readline

K = int(input())
list = []
for _ in range(K):
    a = int(input())
    if a == 0:
        list.pop()
    else:
        list.append(a)
print(sum(list))
