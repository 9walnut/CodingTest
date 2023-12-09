# 최대 상승
n = int(input())
arr = list(map(int, input().split()))
result = 0
minVal = arr[0]
maxVal = 0

for i in range(1, n):
    if minVal < arr[i]:
        result = max(result, arr[i]-minVal)
    else:
        minVal = arr[i]
print(result)
