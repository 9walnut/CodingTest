# 숫자카드2
import sys

N = int(input())
cards = [*map(int, input().split())]
M = int(input())
candidate = [*map(int, input().split())]

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for target in candidate:
    result = count.get(target)
    if result == None:
        print(0, end='')
    else:
        print(result, end='')

# 다른 풀이
input = sys.stdin.readline

N = int(input())
cards = sorted([*map(int, input().split())])
M = int(input())
candidate = [*map(int, input().split())]

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1


def binarySearch(arr, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if arr[mid] == target:
        return count.get(target)
    elif arr[mid] < target:
        return binarySearch(arr, target, mid+1, end)
    else:
        return binarySearch(arr, target, start, mid-1)


for target in candidate:
    print(binarySearch(cards, target, 0, len(cards)-1), end=" ")
