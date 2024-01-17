# 최댓값과 최솟값
def solution(s):
    answer = list(map(int, s.split(' ')))
    answer.sort()
    return str(answer[0]) + " " + str(answer[-1])

# JadenCase 문자열 만들기


def solution(s):
    answer = ''
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    answer = ' '.join(s)
    return answer

# jadenCase 2


def solutsion(s):
    answer = ''
    s = s.split(' ')
    for i in range(len(s)):
        if not s[i][0].isdecimal():
            s[i] = s[i][0].upper() + s[i][1:].lower()
    answer = ' '.join(s)
    return answer
