def solution(progresses, speeds):
    answer = []
    while progresses:
        # 작업 진도가 100% 이상인 기능들을 배포할 수 있는지 확인
        if progresses[0] >= 100:
            count = 0
            # 작업 진도가 100% 이상인 기능들을 모두 제거하고 카운트
            while progresses and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            answer.append(count)

        # 각 기능의 작업 진도를 업데이트
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

    return answer
