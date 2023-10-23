# 백준 10886 - 0 = not cute / 1 = cute
t = int(input())
nocute = 0
cute = 0

for i in range(0, t):
    a = int(input())
    if a == 0:
        nocute += 1
    else:
        cute += 1

if cute > nocute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")

# 백준 10162 - 전자레인지
t = int(input())  # a,b,c 버튼의 총합
if t % 10 != 0:
    print(-1)
else:
    a = b = c = 0
    a = t//300
    b = (t % 300)//60
    c = (t % 300) % 60//10
    print(a, b, c)
