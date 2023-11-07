# 완전 이진 트리
import sys
input = sys.stdin.readline

k = int(input())
nums = list(map(int, input().split()))
nums.reverse()
tree = [0 for i in range(2**k)]


def make_tree(tree, nums, root):
    if root < 1 or 2**k <= root or tree[root] != 0:
        return
    make_tree(tree, nums, 2**root)
    tree[root] = nums.pop()
    make_tree(tree, nums, 2*root + 1)


make_tree(tree, nums, 1)
i = 1
while i < 2 ** k:  # 출력 반복문
    for j in range(i, i * 2):
        print(tree[j], end=' ')
    print()
    i *= 2


# BFS 활용
k = int(input())
_input = list(map(int, input().split()))
tree = [[] for _ in range(k)]


def makeTree(arr, x):
    mid = (len(arr)//2)
    tree[x].append(arr[mid])
    if len(arr) == 1:
        return
    makeTree(arr[:mid], x+1)
    makeTree(arr[mid+1:], x+1)


makeTree(_input, 0)
for i in range(k):
    print(*tree[i])
