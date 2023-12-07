# 골드바흐의 추측
# 소수 판별 함수 작성
# 테스트 케이스, 짝수 입력
# 짝수의 중간 수를 두 개의 변수로 저장
# 0 ~ 중간수까지 소수 함수에 대입
# 소수이면 출력, 아니면 하나씩 더해주고 뺴기

def isPrime(num):
    if num == 1:
        return False
    else:
        # 이해 안가서 여기 암기해야함
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True


t = int(input())

for _ in range(t):
    # 2보다 큰 짝수
    n = int(input())
    # 2로 나누기 때문에 n-tmp가 소수인지 확인이 되어서 나눈 값을 가지고 확인
    tmp = n//2
    while tmp > 0:
        if isPrime(tmp):
            if isPrime(n - tmp):
                print(tmp, n-tmp)
                break
        # 0이 될 때 까지 반복
        tmp -= 1
