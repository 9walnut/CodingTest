# 백설공주와 일곱 난쟁이
# 아이디어
# 입력 값을 모두에 배열에 기입하고 총 합에서 2가지 숫자를 뺀 값이 100인 경우를 찾아서 100이 맞는 경우 배열에서 2 값을 뺌
arr = [int(input()) for _ in range(9)]

arr2 = [0 for _ in range(9)]
breaker = False

for i in range(9):
    # 9 난장이에서 i번째 인덱스에 해당하는 값을 제외한 합
    arr2[i] = sum(arr) - arr[i]
    for j in range(i+1, 9):
        # arr2[i]에서 숫자 하나를 뺀 값이 100이면 정답
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
