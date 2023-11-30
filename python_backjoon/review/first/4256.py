# 트리

import sys
input = sys.stdin.readline


def postorder(preorder, inorder):
    if len(preorder) == 0:
        return
    if len(preorder) == 1:
        result.extend(preorder)
        return
    root = preorder[0]
    inorderidx = inorder.index(root)

    postorder(preorder[1:inorderidx+1], inorder[:inorderidx])
    postorder(preorder[inorderidx+1:], inorder[inorderidx+1:])
    result.append(root)


t = int(input())

for _ in range(t):
    result = []
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    postorder(preorder, inorder)
    print(*result)

# 전위 순회 3214
# 중위 순회 2341
# 후위 순회한 결과를 구하기
# 트리 순서 3 > 왼좌식 2 > 오른자식
