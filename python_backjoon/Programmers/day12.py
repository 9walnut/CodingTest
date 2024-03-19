# 더 맵게(힙)
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        new_s = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville, new_s)
        answer += 1
        if scoville[0] < K and len(scoville) == 1:
            return -1

    return answer

# 디스크 컨트롤러(힙)
# 최소 힙 사용


def solution(jobs):
    answer, now, i = 0
    start = -1  # 초기값 -1 설정
    heap = []  # 작업 저장할 힙

    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:  # 현재 시각 이후 가능한 작업 찾기
                heapq.heappush(heap, [job[1], job[0]])  # 작업 수행 시간 기준 힙에 작업 추가

            if heap:
                current = heapq.heappop(heap)  # 가장 수행시간 짧은 작업 꺼내기
                start = now  # 마지막 작업 시작 시간 현재 시간으로 업데이트
                now += current[0]  # 현재 시간을 처리한 작업 수행 시칸 만큼 증가
                answer += now - current[1]  # 현재 시간 - 작업 요청 시간
                i += 1  # 처리 작업 수
            else:
                now += 1  # 처리 작업 없을 시 현재 시간 1 증가시켜 다음 작업 찾기

    return answer // len(jobs)
