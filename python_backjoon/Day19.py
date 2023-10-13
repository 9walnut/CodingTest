# 별찍기 1 - 2438
t = int(input())

for i in range(1, t+1):
    print("*"*i)

# 팩토리얼 - 10872
t = int(input())
result = 1
for i in range(1, t+1):
    if i <= t :
        result *=i
print(result)

def factorial(t):
    result = 1
    if n > 0:
        result = t*factorial(t-1)
    return result

# 피보나치 수 - 2747
t = int(input())
array = [0, 1]

for i in range(2, t+1):
    array.append(array[-1] + array[-2])
print(array[t])

# 피보나치 수 2747 - 다른풀이
 t = int(input())
 a, b = 0 , 1
 for i in range(t):
    a, b = b, a + b
print(a)

# 별찍기2 - 2439 
t= int(input())
for i in range(1, t+1):
    print(" "*(t-i) + "*"*i)