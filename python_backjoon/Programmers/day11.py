# 각 숫자 떼기
# permutation 활용해서 순열 조합
# .join 활용해서 각각 하나의 숫자로 만들기
# 각 숫자에 대해 소수인지 판별하기

from itertools import permutations


def solution(numbers):
    answer = []
    # 숫자 자르기
    nums = [n for n in numbers]
    per = []
    # 순열 조합 만들기
    for i in range(1, len(numbers)+1):
        per += list(permutations(nums, i))
    # 숫자로 변환
    new_nums = [int("".join(p)) for p in per]

  # 모든 int형 숫자에 대해 소수인지 판별
    for n in new_nums:
        if n < 2:
            continue
        check = True
        for i in range(2, int(n**0.5) + 1):
            if n % 1 == 0:
                check = False
                break
        if check:
            answer.append(n)

    return len(set(answer))
