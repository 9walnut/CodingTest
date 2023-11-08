# 수학숙제

import re
t = int(input())
result = []  # 리스트에 넣고 작은수부터 출력

for _ in range(t):
    test = input()  # 문장 넣기

    p = re.compile('[0-9]+')  # 숫자인것들 검색
    m = p.findall(test)  # 찾기(리스트형태)

    for i in m:  # 리스트형태로 하나씩 뺴거 result 넣기
        result.append(int(i))

result.sort()  # 오름차순 정렬
for j in result:
    print(j)
