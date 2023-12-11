# 퍼즐
from collections import deque
import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    while q:
        now = q.popleft()
        if now == "123456789":
            return cntDict[now]

        # 현재 빈칸 위치
        pos = now.find("9")
        x = pos//3
        y = pos % 3

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 3 and 0 <= ny < 3:
                # 이동할 위치
                nPos = nx*3 + ny
                # 이동상태설정
                nextNum = list(now)
                nextNum[nPos], nextNum[pos] = nextNum[pos], nextNum[nPos]
                nextNum = "".join(nextNum)

                if not cntDict.get(nextNum):
                    # 이동된 상태 저장, 이동횟수 + 1
                    q.append(nextNum)
                    cntDict[nextNum] = cntDict[now] + 1


# 초기 퍼즐 상태
start = ""
for _ in range(3):
    temp = sys.stdin.readline().strip()
    temp = temp.replace(" ", "")
    start += temp

start = start.replace("0", "9")
q = deque()
q.append(start)

cntDict = dict()
cntDict[start] = 0

result = bfs()
print(result if result != None else "-1")
