# 백준 2446 - 별찍기9
t = int(input())

for i in range(t, 0, -1):
  print(" "*(t-i)+"*"*(2*i-1))
for i in range(2, t+1):
  print(" "*(t-i)+"*"*(2*i-1))


# 백준 15894 - 수학은 체육과목입니다.
t = int(input())

print(4*t)

# 백준 10707 - 수도요금
x_a = int(input());
y_b = int(input());
y_c = int(input());
y_d = int(input());
liter = int(input());

x_money = x_a * liter;
y_money = 0;
if liter <= y_c:
  y_money = y_b
elif y_c < liter:
  y_money = y_b + ((liter-y_c)*y_d)

if x_money > y_money :
  print(y_money)
else:
  print(x_money)
  

# 백준 11586 - 지영공주님의 마법 거울
# 2차열 배열 선언 어떻게..? 빈 곳에 집어넣고 싶어요
# 좌우 반전 출력, 상하 반전 출력은 range에서 바꾸면 되는거 같은데....
t = 3
mirror[][]
k = 1
if k==1:
  for i in range(t):
    for j in range(t):
      print(mirror[j], end="")
elif k==2:
  for i in range(t):
    for j in range(t):
      print(mirror[j], end="")
elif k==3:
  for i in range(t):
    for j in range(t):
      print(mirror[j], end="")