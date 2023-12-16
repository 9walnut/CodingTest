import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
LIS = [arr[0]]


def bs(e):
    start = 0
    end = len(LIS)-1

    while start < end:
        mid = (start+end)//2
        if LIS[mid] == e:
            return mid
        elif LIS[mid] < e:
            start = mid+1
        else:
            end = mid
    return start


for i in range(n):
    if LIS[-1] < arr[i]:
        LIS.append(arr[i])
    else:
        idx = bs(arr[i])
        LIS[idx] = arr[i]

print(len(LIS))
