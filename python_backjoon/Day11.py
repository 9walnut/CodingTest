# 백준 4153 - 직각삼각형
while True:
    a = list(map(int, input().split()))
    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        break
    a.sort()
    if a[2]**2 == a[0]**2 + a[1]**2:
        print("right")
    else:
        print("wrong")
# 마지막 줄에 0 0 0이 입력값으로 주어지면서 문제가 끝나기 때문에
# 이와 관련된 조건으로 반복문이 종료되도록 조건문을 만들어줘야함
# 때문에 while문으로 반복문을 만들면서 break를 삽입하여 종료되도록 유도

# 백준 10810 - 공 넣기
# 바구니 n개
# 공 개수 n x n개
# 공 넣으려는 수 m개
n, m = map(int, input().split())
# array[0 ~ 4]
array = [0 for _ in range(n)]
# array = [0]*n 도 가능

for _ in range(m):
    i, j, k = map(int, input().split())
    # i번 바구니부터 j번 바구니까지 공을 넣는 것이기 때문에 j+1
    for idx in range(i, j+1):
        # array 생성시 array[0]부터 생성되었기 때문에 n-1
        array[idx-1] = k

for x in range(n):
    print(array[x], end=" ")
