# 최소 직사각형
def solution(sizes):
    width = []
    height = []

    for size in sizes:
        if size[0] > size[1]:
            width.append(size[0])
            height.append(size[1])
        else:
            width.append(size[1])
            height.append(size[0])

    return max(width) * max(height)

# 모의고사


def solution(answers):
    answer = []
    score = [0, 0, 0]
    std1 = [1, 2, 3, 4, 5]
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == std1[i % 5]:
            score[0] += 1
        if answers[i] == std2[i % 8]:
            score[1] += 1
        if answers[i] == std3[i % 10]:
            score[2] += 1

    for idx, num in enumerate(score):
        if num == max(score):
            answer.append(idx+1)

    return answer
