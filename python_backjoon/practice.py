# a, b = map(int, input().split())
# print(a+b)

print("Hello World")

# 그리디 알고리즘
# 최적의 해를 보장하진 않지만 그리디 탐욕법으로 얻은 해가 최적이라는 추론이 있으면 문제 해결 가능
# 거스름돈 문제
# 가장 큰 화폐 단위부터 거슬러 주기
n =1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n // coin
    n %= coin
    
print(count)

# 1이 될 때까지
n, k = map(int, input().split())
result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 떄까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    
    if n < k:
        break
    result += 1
    n //= k
result += (n-1)
print(result)