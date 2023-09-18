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
a, b = map(int, input().split())
