# 완주하지 못한 선수 - 정렬
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if (participant[i] != completion[i]):
            return participant[i]

    return participant[len(participant)-1]

# 완주하지 못한 선수 - 해시


def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)

    for comp in completion:
        sumHash -= hash(comp)

    return hashDict[sumHash]

# 폰켓몬


def solution(nums):
    dict = {}
    for n in nums:
      # 중복 폰켓몬 수 제거
        dict[n] = 1
        if len(nums) // 2 <= len(dict):
            return len(nums) // 2
    return len(dict)

# 폰켓몬 - set함수 이용


def solution(nums):
    arr = list(set(nums))
    if len(arr) > len(nums)/2:
        return len(nums)/2
    else:
        return len(arr)

# 전화번호 목록
# 접두어 있는 경우 false, 없으면 true


def solution(phone_book):
    answer = True
    # 해시 맵 만들기
    dict = {}
    for pNumber in phone_book:
        dict[pNumber] = 1
    # 접두어가 dict에 있는지 찾기
    for pNumber in phone_book:
        temp = ""
        for num in pNumber:
            temp += num
            # 접두어 찾기 + 기존 번호와 같은 경우 제외
            if temp in dict and temp != pNumber:
                answer = False
    return answer

# 의상


def solution(clothes):
  # 각 종류별 가진 의상 저장
    closet = {}
    for name, kind in clothes:
        if kind in closet.keys():
            closet[kind] += [name]
        else:
            closet[kind] = [name]
    answer = 1
    for _, value in closet.items():
        answer *= (len(value) + 1)
        # 아무것도 입지 않은 경우 제외
    return answer - 1
