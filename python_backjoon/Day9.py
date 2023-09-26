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
