# 괄호
import sys
t = int(input())

for i in range(t):
    stack = []
    a = sys.stdin.readline()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
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
