# 괄호
import sys
N = int(input())

for i in range(N):
    stack = []
    a = sys.stdin.readline()
    for j in range(a):
        if j == "(":
            stack.append(i)
        elif j == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
        else:
            if not stack:
                print("YES")
            else:
                print("NO")
