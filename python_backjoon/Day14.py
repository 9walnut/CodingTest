# 백준 4344 - 평균은 넘겠지
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
