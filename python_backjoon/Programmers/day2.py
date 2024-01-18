# 최소값 만들기

def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort()
    for i in range(len(A)):
        answer += (A[i]*B[i])

    return answer

  # 올바른 괄호


def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append('(')
        else:
            if stack == []:
                return False
            else:
                stack.pop()
    if stack != []:
        return False
    return True

# 같은 숫자는 싫어


def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])

    return answer

# 기능개발


def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        while progresses and progresses[0] >= 100:
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)

        progresses = [progresses[i]+speeds[i] for i in range(len(progresses))]

        if cnt:
            answer.append(cnt)
    return answer
