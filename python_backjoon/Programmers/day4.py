# 정렬

# K번째 수
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        cut = array[commands[i][0]-1:commands[i][1]]
        cut.sort()
        answer.append(cut[commands[i][2]-1])
    return answer

# 가장 큰 수


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
