# OX 퀴즈
t = int(input())

for i in range(t):
    arr = input()
    score = 0
    sum_score = 0
    for j in range(len(arr)):
        if arr[j] == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)
