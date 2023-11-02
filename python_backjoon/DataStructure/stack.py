# 스택 - 10828
import sys

t = int(sys.stdin.readline())
stack = []

for _ in range(t):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)


# 괄호 - 9012
t = int(sys.stdin.readline())

for i in range(t):
    stack = []
    a = sys.stdin.readline()
    for j in a:
        if j == "(":
            stack.append(j)
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


# 수 찾기 - 1920
