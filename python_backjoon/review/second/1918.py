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
          # 스택 마지막이면 )을 스택에 추가 ex) (A+B)
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(s)
            # ")"은 stack에 삽입할일 없이 전 문자를 비교
            # 이전 스택이 "("일 경우 스택에서 바로 pop
            # 아닌경우 이전 스택에 있는 문자열 빼서 결과 기입
        elif s == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()
print(res)
