# 후위표식기
n = list(input())
stack = []
res = ""

for s in n:
    if s.isalpha():
        res += s
    else:
        if s == "(":
            stack.append(s)
        elif s == "*" or s == '/':
          # 스택에 * 혹은 / 이 있는 경우 res에 추가
            while stack and (stack[-1] == "*" or stack[-1] == '/'):
                res += stack.pop()
          # 없다면 바로 stackdp s 추가
            stack.append(s)
        elif s == "+" or s == "-":
          # 스택의 마지막에 (  이 아니라면 res에 추가
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(s)
        elif s == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()
print(res)