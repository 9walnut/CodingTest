# 백준 11021 - A+B-7
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# input함수로 입력을 받고 정수로 변환
X = int(input())
# for문으로 반복문 작성
for i in range(1, X+1):
#     # A, B 두 수를 공백으로 구분한 하나의 문장으로 입력, split 함수 괄호에 아무것도 입력하지 않으면 공백을 기준으로 나눌 수 있음
#     # 두 수를 한번에 int 타입으로 변환하기 위해 map 함수 사용
    A, B = map(int, input().split())
#     # 문자형과 같이 사용하기 위해 자료형인 str(i)를 사용
    print("Case #" + str(i) + ":", A+B)
    
# 백준 11022 - A+B-8
X = int(input())
for i in range(1, X+1):
    A, B = map(int, input().split())
    print("Case #%d: %d + %d = %d" %(i, A, B, A+B))
    
# 백준 10699 - 오늘 날짜
# 파이썬 내장 모듈 중 하나로, 날짜와 시간을 다루는 클래스와 함수 제공
# date.time.date는 날짜 정보를 저장하는데 사용 / 연월일 정보를 가지는 객체 생성
import datetime
d_today = datetime.date.today()
print(d_today)

# 백준 7287 - 등록
print("3")
print("kguho9202")

# 백준 2525 - 오븐시계
# 변수를 할 줄에 입력
hour, min = map(int, input().split())
c = int(input()) # 요리에 필요한 시간

hour += c//60 #c를 60으로 나누어 시간 단위로 나눈 뒤 hour값에 더하기
min += c%60 #c를 60으로 나누어 시간으로 나눈 값의 나머지를 mon값에 더하기

# min값이 60보다 초과되면 60을 빼고 시간 +
if(min >= 60):
    hour +=1
    print(hour%24, min-60)
else:
    print(hour%24, min)
    
# 백준 2530 - 인공지능 시계
A, B, C = map(int, input().split())
D = int(input())

result=A*3600+B*60+C+D
print(result//3600%24, result//60%60, result%60)

# 백준 2914 - 저작권
# 앨범 수록곡 개수 a, 평균값 i
# 구하려는 값은 저작권이 있는 멜로디
# i는 평균의 올림값이기 때문에 
# 저작권 멜로디의 최소값는 a*(i-1)에서 +1을해주면 평균값이 올림값이 됨
a, i = map(int, input().split())
print(a*(i-1)+1)

# 백준 5355 - 화성수학
# 테스트 케이스 개수
t = int(input())

# t에 저장된 케이스 수만큼 반복
for i in range(t):
    # l에 문자열을 입력받아 분할
    l = list(map(str, input().split()))

    # 매개변수로 받은 식을 문자열로 받아 실행하는 함수(eval)
    result = eval(l[0])
    
    # l의 길이만큼 반복
    for j in range(len(l)):
        if l[j] == '@':
            result *= 3
        elif l[j] == '%':
            result += 5
        elif l[j] == '#':
            result -= 7
    print("%0.2f" %result)
    
# 백준 2675 - 문자열 반복
t = int(input())
    
for i in range(t):
    r, s = input().split()
    for j in s:
        print(j*int(r), end = "") #end를 활용한 공백 없애기
    print()