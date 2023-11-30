# 백설공주와 일곱 난쟁이
arr = [int(input()) for _ in range(9)]
arr2 = [0 for _ in range(9)]
breaker = False

for i in range(9):
    arr2[i] = sum(arr) - arr[i]
    for j in range(i+1, 9):
        if arr2[i] - arr[j] == 100:
            a, b = arr[i], arr[j]
            arr.remove(a)
            arr.remove(b)
            breaker = True
            break
    if breaker == True:
        break

for i in range(7):
    print(arr[i])
