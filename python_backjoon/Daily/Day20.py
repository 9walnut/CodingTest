# 1408 - 24
h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))
t = h2*3600 + m2*60 + s2 - (h1*3600+m1*60+s1)
if t < 0:
    t += 24*60*60
h = t//3600
m = (t % 3600)//60
s = t % 60

print("%02d:%02d:%02d" % (h, m, s))

# 2839 - 구구단
t = int(input())

for i in range(1, 10):
    print("%d * %d = %d" % (t, i, t*i))

# 별찍기 -3
t = 5
for i in range(1, t+1):
    print("*"*(t-i+1))
