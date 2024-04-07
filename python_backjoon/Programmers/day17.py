# 이분탐색

def solution(n, times):
    answer = 0
    # right는 가장 비효율적으로 심사했을 때 걸리는 시간
    # 가장 긴 심사시간이 소요되는 심사관에게 n 명 모두 심사받는 경우이다.
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            # people 은 모든 심사관들이 mid분 동안 심사한 사람의 수
            people += mid // time
            # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나간다.
            if people >= n:
                break

        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        if people >= n:
            answer = mid
            right = mid - 1
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
        elif people < n:
            left = mid + 1

    return answer


def solution(distance, rocks, n):
    # 커트라인 최솟값 = 1
    left = 1
    # 커트라인 최댓값 = distance
    right = distance

    # 바위 위치를 정렬하고, 도착지점 append
    rocks.sort()
    rocks.append(distance)

    while left <= right:
        mid = (left+right)//2
        # 제거한 바위 개수
        delete = 0
        # 이전 바위의 위치
        prev_rock = 0
        for rock in rocks:
            dist = rock - prev_rock
            # 거리가 커트라인 보다 작다면, 바위를 제거
            if dist < mid:
                delete += 1
                # 제거한 바위가 너무 많다면 break
                if delete > n:
                    break
            # 바위를 제거하지 않았다면, prev_rock을 갱신
            else:
                prev_rock = rock

        # 초과 제거한 경우 : 커트라인이 너무 높음
        if delete > n:
            right = mid - 1
        # 이하 제거한 경우 : 커트라인이 적절하거나 너무 낮음
        else:
            answer = mid
            left = mid + 1
    return answer
