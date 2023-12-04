# 먹을 것인가 먹힐 것인가
import sys
input = sys.stdin.readline


def bs(li, a):
    s, e = 0, len(li) - 1
    res = -1
    while s <= e:
        m = (s+e)//2
        if li[m] < a:
            res = m
            s = m+1
        else:
            e = m-1
    return res


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    for a in A:
        cnt += (bs(B, a)+1)
    print(cnt)
