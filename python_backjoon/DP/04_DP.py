# 피보나치 함수 - 1003
t = int(input())
for _ in range(t):
    n = int(input())
    count_0 = [1, 0]
    count_1 = [0, 1]
    for _ in range(2, n+1):
        count_0.append(count_1[-1])
        count_1.append(count_0[-2]+count_0[-1])
    print(count_0[n], count_1[n])
