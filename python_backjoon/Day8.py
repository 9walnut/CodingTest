# 백준 11721 - 열개씩 끊어 출력하기
t = input()

for i in range(0, len(t), 10):
  print(t[i:i+10])

# 백준 10988 - 팰린드롬인지 확인하기
  
t = list(str(input()))

if list(reversed(t)) == t :
  print(1)
else :
  print(0)

  # 백준 28014 - 첨탑밀어서 부수기
n = int(input())
tower_high = list(map(int, input().split()))
result = 1

for i in range(n-1):
  if tower_high[i] <= tower_high[i+1]:
    result += 1
print(result)

