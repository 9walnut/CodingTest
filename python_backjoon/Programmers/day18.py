import sys
from collections import deque


def solution(operations):
    answer = []

    queue = deque()  # 큐 생성
    for i in operations:
        li = list(i.split())  # 공백 기준으로 분리하여 리스트 저장
        if (li[0] == "I"):
            queue.append(int(li[1]))  # 값을 정수로 큐에 추가
        else:
            if (len(queue) != 0):
                if (int(li[1]) == 1):
                    queue.pop()
                else:
                    queue.popleft()

        queue = deque(sorted(queue))

    if (len(queue) == 0):
        answer = [0, 0]
    else:
        answer = [max(queue), min(queue)]

    return answer


# 단어 변환(BFS)


def solution(begin, target, words):

    if target not in words:
        return 0

    return bfs(begin, target, words)


# 최소 단계를 찾아야 하므로 bfs
def bfs(begin, target, words):

    queue = deque()
    queue.append([begin, 0])  # 시작 단어와 단계 0으로 초기화

    while queue:
        now, step = queue.popleft()

        if now == target:
            return step

        # 단어를 모두 체크하면서, 해당 단어가 변경될 수 있는지 체크
        for word in words:
            count = 0
            for i in range(len(now)):  # 단어의 길이만큼 반복하여
                if now[i] != word[i]:  # 단어에 알파벳 한개씩 체크하기
                    count += 1

            if count == 1:
                queue.append([word, step+1])

# 네트워크(BFS)


def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]

    for com in range(n):
        if visited[com] == False:
            # 컴퓨터 수, 컴퓨터들 연결된 리스트, 현재 방문중인 인덱스, 방문 컴퓨터 표시
            BFS(n, computers, com, visited)
            answer += 1  # 빠져나오게 되면 하나의 네트워크로 체크
    return answer


def BFS(n, computers, com, visited):
    visited[com] = True
    queue = []
    queue.append(com)
    while len(queue) != 0:
        com = queue.pop(0)
        visited[com] = True
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:  # 연결된 컴퓨터
                if visited[connect] == False:
                    queue.append(connect)


def solution(N, number):
    # s[i] : 주어진 수 N을 i+1번 사용해서 만들 수 있는 수들의 집합
    # set 8개 초기화, 왜 8개를 만드냐? N 사용횟수가 8보다 크면 -1을 return하므로 N을 1개부터 8개 까지 사용하여 만든 값들이 number가 안될 경우 -1을 return한다.
    s = [set() for x in range(8)]
    # 보통 첫번째 원소의 idx는 0인데 여기서는 첫번째 원소의 idx를 1로 시작한다.
    for i, x in enumerate(s, start=1):
        # 8개의 set 각각 초기화, s[0] = N, s[1] = NN ... s[7] = NNNNNNNN (8개)
        x.add(int(str(N) * i))
    # s[i] 즉 N을 i+1개 사용했을 때 만들 수 있는 숫자 구하기.
    for i in range(len(s)):
        for j in range(i):
            for op1 in s[j]:  # op1 : 피연산자1, N을 j+1번 사용하여 만들 수 있는 숫자들
                for op2 in s[i-j-1]:  # op2 : 피연산자2, N을 i-j번 사용하여 만들 수 있는 숫자들
                    # op1과 op2를 사칙연산 --> 즉 N을 i+1번 사용하여 만들 수 있는 숫자를 구하게 되고 이를 s[i]에 대입
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        if number in s[i]:  # N을 i+1번 사용했을 때 찾고자하는 값 number가 존재한다면 i+1 return
            answer = i + 1
            break
        else:  # N을 8번 사용했는데도 찾고자하는 값 number가 존재하지 않는다면 -1 return
            answer = -1
    return answer


N, L = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def check(line, L):
    # 경사로 생기는 곳 체크
    visited = [False for _ in range(N)]
    # 자리 차례로 탐색
    for i in range(0, N-1):
        # 바로 다음 위치의 높이가 같으면 continue
        if line[i] == line[i+1]:
            continue
        # 다음 위치의 높이 차이가 1 넘게 나면 False
        elif abs(line[i]-line[i+1]) > 1:
            return False
        # 현재 높이가 다음 높이 보다 높으면 오른쪽 높이가 같은지 체크
        elif line[i] > line[i+1]:
            temp = line[i+1]  # 다음 높이
            for j in range(i+1, i+L+1):
                # 경사 길이가 범위 안이면
                if 0 <= j < N:
                    # 경사 놓을 위치의 높이가 하나라도 다르면
                    if temp != line[j]:
                        return False
                    # 높이는 다 같은데 이미 경사가 놓여진 곳이면
                    elif visited[j]:
                        return False
                    # 경사 놓기
                    visited[j] = True
                # 경사 길이가 범위 벗어나면
                else:
                    return False
        # 다음 높이가 현재 높이 보다 높으면 왼쪽 높이가 같은지 체크
        else:
            temp = line[i]
            for j in range(i, i-L, -1):
                # 경사 길이가 범위 안이면
                if 0 <= j < N:
                    # 경사 놓을 위치의 높이가 하나라도 다르면
                    if temp != line[j]:
                        return False
                    # 높이는 다 같은데 이미 경사가 놓여진 곳이면
                    elif visited[j]:
                        return False
                    # 경사 놓기
                    visited[j] = True
                # 경사 길이가 범위 벗어나면
                else:
                    return False
    return True


answer = 0
# 가로 길 체크
for i in board:
    if check(i, L):
        answer += 1

# 세로 길을 체크하기 위해 변환해서 넣어줌
for i in range(N):
    temp = []
    for j in range(N):
        temp.append(board[j][i])
    if check(temp, L):
        answer += 1

print(answer)


N = int(input())

dx = [-1, 0, 0, 1]  # 상 좌 우 하
dy = [0, -1, 1, 0]
room = []
sharksize = 2
sharkeat = 0

for i in range(N):
    room.append([int(x) for x in sys.stdin.readline().rstrip().split()])
    for j in range(len(room[i])):
        if room[i][j] == 9:
            room[i][j] = 0
            shark_x, shark_y = i, j


def finding_fish(sx, sy):
    global sharksize
    deq = deque()
    deq.append([sx, sy])

    visited = [[False for _ in range(N)] for _ in range(N)]
    distance = [[0 for _ in range(N)] for _ in range(N)]
    can_eat_fish = []

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if room[nx][ny] <= sharksize and not visited[nx][ny]:  # 이동이 가능하면
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    deq.append([nx, ny])

                    if room[nx][ny] < sharksize and room[nx][ny] != 0:  # 물고기가 있고 그걸 먹을 수 있다면
                        can_eat_fish.append([nx, ny, distance[nx][ny]])

    can_eat_fish.sort(key=lambda x: (x[2], x[0], x[1]))  # 정렬은 거리, x, y 오름차순으로
    return can_eat_fish


if __name__ == '__main__':
    ans = 0

    while True:
        fishlist = finding_fish(shark_x, shark_y)

        if len(fishlist) == 0:  # 먹을 수 있는 물고기가 없다면
            print(ans)
            exit(0)

        shark_x, shark_y, move_time = fishlist[0]

        sharkeat += 1
        if sharksize == sharkeat:  # 먹은 물고기수와 사이즈가 같다면
            sharkeat = 0
            sharksize += 1

        room[shark_x][shark_y] = 0  # 물고기 먹은 자리는 빈칸으로 바꿈
        ans += move_time


def solution(N, number):
    dp = [set() for i in range(9)]  # 사용횟수에 따라 가능한 숫자를 담을 리스트
    for i in range(1, 9):  # 1~8
        dp[i].add(int(str(N)*i))  # 단순히 이어붙인 숫자
        for j in range(i//2 + 1):
            for first in dp[j]:
                for second in dp[i-j]:
                    dp[i].add(first + second)
                    dp[i].add(first - second)
                    dp[i].add(second - first)
                    dp[i].add(first * second)
                    if second != 0:
                        dp[i].add(first // second)
                    if first != 0:
                        dp[i].add(second // first)

        if number in dp[i]:
            return i
    return -1
