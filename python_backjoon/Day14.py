# 백준 4344 - 평균은 넘겠지
from bisect import bisect_left, bisect_right
t = int(input())

for i in range(t):
    array = list(map(int, input().split()))
    avg = sum(array[1:])/array[0]

    count = 0
    for i in array[1:]:
        if i > avg:
            count += 1
    per = (count/array[0])*100
    print("%.3f" % per + "%")

# 백준 1110 - 더하기 싸이클
t = 55
d = t
count = 0

while True:
    # 십의 자리
    a = d//10
    # 한자리수
    b = d % 10
    # 새로운 수
    c = (a+b) % 10
    d = (b*10)+c
    count += 1

    if (t == d):
        break
print(count)
# 왜 꼭 d를 변수로 선언해야만 진행이 되는거지?

# 백준 4796 - 캠핑
i = 0
while True:
    i += 1
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    a = v//p
    b = v % p
    if l < b:
        b = l

    print("Case %d: %d" % (i, l*a+b))

# 이것에코테다 - 이진탐색
# 파라메트릭 서치
# 조건의 만족여부를 확인해서 탐색 범위를 좁혀가야함
a, b = list.map(int, input().split(" "))
array = list(map(int, input().split()))

# 떡길이 19cm
# 시작점 0 끝점 19 중간점 9
# 잘린 값이 M보다큰 25이기 때문에 중간점(오른쪽으로) 이동

# 시작점과 끝점 선정
start = 0
end = max(array)

# 이진탐색 수행(반복적)
result = 0
while (start <= end):
    total = 0
    mid = (start+end)//2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡 양이 부족한 경우 더 많이 자르기
    if total < b:
        end = mid - 1
    # 떡의 양이 더 많은 경우 더 조금 자르기
    else:
        result = mid  # 최대한 덜 자른 것이 정답이므로 여기에서 result 기록
        start = mid + 1
print(result)


def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    return right_index-left_index


n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)
