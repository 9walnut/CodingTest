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
