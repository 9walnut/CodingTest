# 백준 2693 - n번재 큰 수
t = int(input())

for i in range(t):
    array = list(map(int, input().split()))
    array.sort()
    # 3번째 큰수 이니까 뒤에서 3번째 숫자 출력
    print(array[-3])

# 백준 1546 - 평균
t = int(input())
array = list(map(int, input().split()))
array.sort()
max_value = array[-1]

for i in range(t):
    array[i] = array[i]/max_value*100
print(sum(array)/t)
