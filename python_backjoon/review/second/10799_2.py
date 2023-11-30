# 쇠막대기
N = int(input())
stack = []
answer = 0

for i in range(N):
    if N[i] == '(':
        stack.append('(')
    else:
        if N[i-1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1

print(answer)
