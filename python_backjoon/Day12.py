# 백준 13777 - Hunt the Rabbit
# 함수 정의 및 매개변수 정의
def binary_search(target, envelopes):
    left, right = 0, len(envelopes) - 1
    opened = []

    while left <= right:
        mid = (left + right) // 2
        opened.append(envelopes[mid])

        if envelopes[mid] == target:
            return opened
        elif envelopes[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return opened


envelopes = list(range(1, 51))  # 1부터 50까지의 봉투 번호 생성
while True:
    target = int(input())
    if target == 0:
        break

    opened = binary_search(target, envelopes)

    # 결과 출력
    print(" ".join(map(str, opened)))


# 백준 5585 - 거스름돈
t = 720
changes = [500, 100, 50, 10, 5, 1]

result = 0
for change in changes:
    if t == 0:
        break
    result += t//change
    t = t % change

print(result)
