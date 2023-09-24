# 백준 2444 - 별찍기7
t = int(input())

for i in range(1, t+1):
    print(" "*(t-i) + "*"*(2*i-1))
for i in range(t-1, 0, -1):
    print(" "*(t-i) + "*"*(2*i-1))


# 백준 2443 - 별찍기6
t = int(input())

for i in range(t, 0, -1):
    print(" "*(t-i) + "*"*(2*i-1))
