# 지영 공주님의 마법 거울 - 풀이(1)
t = int(input())
result = []

for row_index in range(t):
    row = input()
    result.append(row)

n = int(input())
if n == 1:
    for row in result:
        print(row)
elif n == 2:
    for row in result:
        print(row[::-1])
elif n == 3:
    for row_index in range(-1, -t-1, -1):
        print(result[row_index])

# 지영 공주님 - 풀이(2)
n = int(input())
mirror = [input() for _ in range(t)]
k = int(input())

# *list 는 언패킹 - 한변수의 데이터를 각각의 변수로 반환
if k == 1:
    print(*mirror, sep='\n')
elif k == 2:
    print(*[i[::-1] for i in mirror], sep='\n')
elif k == 3:
    print(*mirror[::-1], sep='\n')
