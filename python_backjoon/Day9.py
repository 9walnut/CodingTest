# 백준 2563 - 색종이
n = int(input())
arry = [[0 for j in range(100)] for i in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arry[i][j] = 1

result = 0
for k in arry:
    result += k.count(1)

print(result)

# 백준 1152 - 단어의 개수
string = input()

print(len(string.split()))


# 백준 2750 - 수 정렬하기
# 중복값이 없는데 그냥 sort해버리는게 의문
n = int(input())
list = []

for i in range(n):
    list.append(int(input()))

list.sort()

for i in list:
    print(i)

#  백준 2577 - 숫자의 개수
num1 = int(input())
num2 = int(input())
num3 = int(input())

result = list(str(num1*num2*num3))

# 0 ~ 9까지의 숫자를 세는 것이기 때문에 length 대신 10
for i in range(10):
    print(result.count(str(i)))

# 백준 8958 - OX퀴즈
t = int(input())

for i in range(t):
    # 케이스 값 받아주기
    l = input()
    score = 0
    sum_score = 0
    for j in range(len(l)):
        # 배열이 O이면 score 1 추가
        if l[j] == 'O':
            score += 1
            sum_score += score
        # 배열이 X이면 score 초기화
        elif l[j] == 'X':
            score = 0
    print(sum_score)

# 백준 1089 - 알파벳 찾기
s = str(input())
# 문자열도 인덱스로 접근 가능하기에 문자열을 활용한 반복문으로 해결
c = 'abcdefghijklmnopqrstuvwxyz'

for i in c:
    if i in s:
        print(s.index(i), end=" ")
    else:
        print("-1", end=" ")

# 아스키 코드를 활용한 풀이
s = input()
alphabet = list(range(97, 123))

for i in alphabet:
    # chr() : 아스키코드 숫자를 문자로 변환
    # find() : 찾는 문자가 문자열에 있으면 인덱스를, 없다면 -1반환
    # find는 문자열에서만 사용 가능하다
    print(s.find(chr(i)))
