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
