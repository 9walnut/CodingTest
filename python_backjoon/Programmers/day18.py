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
