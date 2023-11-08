# 파일 정리
import sys
input = sys.stdin.readline
n = int(sys.stdin.readline())

arr = []
dict = {}

for i in range(n):
    file = input().split('.')
    arr.append(file[1])

for i in arr:
    if dict.get(i):
        dict[i] += 1
    else:
        dict[i] = 1

dict = sorted(dict.items())

for i, j in dict:
    print(i, j)


# 다른 풀이
input = sys.stdin.readline
n = int(input().rstrip())
file = {}

for _ in range(n):
    filename = input().rstrip().split('.')

    if filename[1] in file:
        file[filename[1]] += 1
    else:
        file[filename[1]] = 1

file = sorted(file.items(), key=lambda x: x[0], reverse=False)

for i in file:
    print(i[0], i[1])
